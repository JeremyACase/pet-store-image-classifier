from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image
import logging

import classify_animal

# Set up Flask app
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to accept image via POST request
@app.route('/upload-image', methods=['POST'])
def upload_image():
    try:
        # Check if an image file is part of the request
        if 'image' not in request.files:
            logger.error("No image part in the request")
            return jsonify({"error": "No image part in the request"}), 400
        
        file = request.files['image']
        
        # Check if a file was selected
        if file.filename == '':
            logger.error("No selected file")
            return jsonify({"error": "No selected file"}), 400
        
        # Validate file extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Save the image temporarily
            file.save(file_path)
            logger.info(f"Image saved to {file_path}")
            
            # Optional: Verify the image can be opened
            try:
                img = Image.open(file_path)
                img.verify()  # Verify it's a valid image
                img.close()
            except Exception as e:
                logger.error(f"Invalid image file: {e}")
                os.remove(file_path)  # Clean up
                return jsonify({"error": "Invalid image file"}), 400
            
            inference = classify_animal.classify_image_with_binary(file_path)

            # Clean up the temporary file (optional)
            os.remove(file_path)
            logger.info(f"Temporary file {file_path} removed")
            
            return jsonify(inference), 200
        
        else:
            logger.error("Invalid file type")
            return jsonify({"error": "Invalid file type. Allowed: png, jpg, jpeg, gif"}), 400
    
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Run the app
if __name__ == '__main__':
    logger.info("Starting Flask RESTful service...")
    app.run(host='0.0.0.0', port=5000, debug=True)