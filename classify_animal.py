import subprocess
import os
import requests
from io import BytesIO
from PIL import Image

# Function to download a sample animal image from the web
def download_animal_image():
    # Using a public domain image of a cat as an example
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    # Save the image locally
    img_path = "animal_image.jpg"
    img.save(img_path)
    return img_path

# Function to run the Hugging Face binary with the image
def classify_image_with_binary(image_path, binary_path):
    # Check if the binary and image exist
    if not os.path.exists(binary_path):
        raise FileNotFoundError(f"The binary file {binary_path} does not exist.")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file {image_path} does not exist.")
    
    # Construct the command to run the binary
    # Replace 'hf_classifier' with the actual name of your binary
    # Adjust the command syntax based on your binary's requirements
    command = [binary_path, image_path]
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Classification Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running the binary: {e}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Path to your Hugging Face binary (update this to your actual binary path)
    binary_path = "C:\\Users\\Jerem\\.cache\\huggingface\\hub\\models--Fabiuas--Animal-classifier\\snapshots\\09f1b0369bdb3e3bf5170e906f3cecc26feef079\\pytorch_model.bin"  # Example: "/path/to/your/hf_classifier"
    
    # Download an animal image
    print("Downloading a sample animal image...")
    image_path = download_animal_image()
    
    # Run the classification
    print(f"Sending image to classifier at {binary_path}...")
    classify_image_with_binary(image_path, binary_path)
    
    # Clean up the downloaded image (optional)
    if os.path.exists(image_path):
        os.remove(image_path)
        print("Temporary image file removed.")