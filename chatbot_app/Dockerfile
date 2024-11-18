# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y curl

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

RUN chmod +x install_ollama.sh && ./install_ollama.sh

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]