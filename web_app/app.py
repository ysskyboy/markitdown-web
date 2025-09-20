from flask import Flask, request, render_template, jsonify, send_file
import os
import tempfile
from markitdown import MarkItDown
import traceback

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Initialize MarkItDown
markitdown = MarkItDown()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Create a temporary file to save the uploaded file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            file.save(tmp_file.name)
            tmp_filename = tmp_file.name

        # Convert the file using MarkItDown
        result = markitdown.convert(tmp_filename)

        # Clean up the temporary file
        os.unlink(tmp_filename)

        # Return the markdown content
        return jsonify({'markdown': result.text_content})

    except Exception as e:
        # Clean up the temporary file if it exists
        if 'tmp_filename' in locals():
            try:
                os.unlink(tmp_filename)
            except:
                pass
        return jsonify({'error': f'Conversion failed: {str(e)}', 'traceback': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)