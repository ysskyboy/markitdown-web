# MarkItDown Web Interface

A web interface for the MarkItDown document converter that allows you to convert various document formats to Markdown through a simple web UI.

## Features

- Convert PDF, Word, Excel, PowerPoint, Images, and more to Markdown
- Drag and drop file upload
- Copy to clipboard functionality
- Responsive design

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Navigate to the web_app directory:
   ```
   cd web_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000`

3. Upload a document file using the interface

4. Click "Convert to Markdown" to convert the file

5. View the resulting Markdown in the text area and copy it to your clipboard if needed

## Supported File Types

MarkItDown supports conversion from:
- PDF
- Word (.doc, .docx)
- Excel (.xls, .xlsx)
- PowerPoint (.ppt, .pptx)
- Images (.jpg, .jpeg, .png, .gif, .bmp)
- Audio (.mp3, .wav)
- Text-based formats (.txt, .csv, .xml, .html)
- ZIP files
- YouTube URLs
- EPubs
- And more!

## Development

To modify the application:

1. Edit `app.py` for backend changes
2. Edit `templates/index.html` for frontend changes
3. Restart the Flask server to see changes

## License

This project is licensed under the MIT License - see the main MarkItDown project for details.