from flask import Flask, render_template, request, jsonify
import os

# Create a simple Flask app without markitdown dependency
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    return jsonify({'markdown': '# Sample Markdown\n\nThis is a sample markdown content.\n\n- Item 1\n- Item 2\n- Item 3'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)