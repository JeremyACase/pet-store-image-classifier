import subprocess
import sys
import os
import requests
from io import BytesIO
from PIL import Image
from transformers import pipeline

# Function to run the Hugging Face binary with the image
def classify_image_with_binary(image_path):
    
    # Load pipeline with your local model
    pipe = pipeline("image-classification", model = "./model/")

    # Load the image you want to send for inference
    image = Image.open(image_path)

    # Run inference
    results = pipe(image)

    return results