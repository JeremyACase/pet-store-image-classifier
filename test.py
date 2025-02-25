import torch
from torchvision import transforms
from PIL import Image
import subprocess
import json

# Path to the local binary model
MODEL_PATH = "C:\\Users\\Jerem\\.cache\\huggingface\\hub\\models--Fabiuas--Animal-classifier\\snapshots\\09f1b0369bdb3e3bf5170e906f3cecc26feef079\\pytorch_model.bin"
IMAGE_PATH = "./animal_image.jpg"  # Path to the image

def preprocess_image(image_path):
    """Preprocess the image for the model."""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Adjust as needed
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

def run_model(image_path):
    """Run the model binary with the given image."""
    try:
        result = subprocess.run([MODEL_PATH, image_path], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)  # Assuming JSON output
    except subprocess.CalledProcessError as e:
        print("Error running model:", e)
        return None

if __name__ == "__main__":
    image_tensor = preprocess_image(IMAGE_PATH)
    classification_result = run_model(IMAGE_PATH)
    print("Classification Result:", classification_result)