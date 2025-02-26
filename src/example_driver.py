import requests

# This is an example driver script to upload an image to our classification service for inference.

# Flask server URL
url = "http://127.0.0.1:5000/upload-image"

# Image file to upload
image_path = "smoke_test.png"  

# Open the file in binary mode
with open(image_path, "rb") as image_file:
    files = {"image": image_file}

    # Send POST request
    response = requests.post(url, files=files)

# Print the server response
print(response.json())