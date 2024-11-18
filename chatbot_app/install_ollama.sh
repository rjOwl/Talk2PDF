#!/bin/bash

# Function to check if ollama is installed
is_ollama_installed() {
    command -v ollama >/dev/null 2>&1
}

# Function to check if ollama is running
is_ollama_running() {
    if sudo service ollama status >/dev/null 2>&1; then
        return 0  # ollama is running
    else
        return 1  # ollama is not running
    fi
}

# Function to check if the mistral model already exists
is_model_installed() {
    ollama list | grep -q "mistral"
}

# Check if ollama is installed
if is_ollama_installed; then
    echo "Ollama is already installed."
else
    echo "Ollama is not installed. Installing..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Check if ollama is running
if is_ollama_running; then
    echo "Ollama is already running."
else
    echo "Starting Ollama..."
    ollama start &
fi

# Check if the mistral model is already installed
if is_model_installed; then
    echo "Mistral model is already installed."
else
    echo "Pulling the mistral model..."
    ollama pull mistral
fi