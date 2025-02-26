FROM python:3.11-slim

ENV PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U "huggingface_hub[cli]"

# Download and install our model and model configs
RUN huggingface-cli download Fabiuas/Animal-classifier pytorch_model.bin --local-dir=./model
RUN huggingface-cli download Fabiuas/Animal-classifier config.json --local-dir=./model
RUN huggingface-cli download Fabiuas/Animal-classifier preprocessor_config.json --local-dir=./model

# Copy the rest of the application code
COPY src/ .

EXPOSE ${PORT}

# Define the command to run the application
CMD ["python", "app.py"]