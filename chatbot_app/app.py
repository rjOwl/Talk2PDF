from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from utils.pdf_handler import extract_text
from utils.chatbot import get_response
from llm_api.populate_database import prepare_db
from llm_api.query_data import query_rag

import shutil
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'llm_api/pdf_files'  # Specify the directory to save uploaded files
WORKING_FOLDER = 'llm_api/pdf_files/context'  # Specify the directory to save uploaded files
CHROMA_FOLDER = 'llm_api/chroma'  # Specify the directory to save uploaded files
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the directory if it doesn't exist
os.makedirs(CHROMA_FOLDER, exist_ok=True)  # Create the directory if it doesn't exist
os.makedirs(WORKING_FOLDER, exist_ok=True)  # Create the directory if it doesn't exist

# Serve the main React app
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

def prepare_context():
    pass

# Endpoint for document upload
@app.route('/upload', methods=['POST'])
def upload_document():
    reset = False
    print("# FILENAME BEFORE: ", request.files)
    if 'file' not in request.files:
        print("# ERRORRRR FILENAME BEFORE: ")
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    print("# FILENAME IS: ", file.filename)

    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file_path_working_dir = os.path.join(WORKING_FOLDER, file.filename)

        # Check if the file already exists in UPLOAD_FOLDER
        if os.path.exists(file_path) and not os.path.exists(file_path_working_dir):
            print("File already exists in UPLOAD_FOLDER. Moving existing files in WORKING_FOLDER back one directory.")
            # Move existing files in WORKING_FOLDER back one directory
            for filename in os.listdir(WORKING_FOLDER):
                source_path = os.path.join(WORKING_FOLDER, filename)
                destination_path = os.path.join(UPLOAD_FOLDER, filename)
                
                if os.path.isfile(source_path):  # Ensure it's a file
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} -> {destination_path}")

            # Move the new file to WORKING_FOLDER
            shutil.move(file_path, os.path.join(WORKING_FOLDER, file.filename))

            # reset the db context and embedding
            reset=True
        # If the file does not exist in UPLOAD_FOLDER, save it
        elif not os.path.exists(file_path) and not os.path.exists(file_path_working_dir):
            file.save(file_path_working_dir)

            # reset the db context and embedding
            reset=True
        else:
            print("File is used in context.")

        prepare_db(reset)

        # # TODO: repalce it with the database save and embedding
        # text = "extract_text(file)"

        # Store text in a suitable way (e.g., in memory or database)
        return jsonify({"message": "Document uploaded successfully"}), 200

    return jsonify({"error": "Invalid file format"}), 400

# Endpoint for chatbot interaction
@app.route('/ask', methods=['POST'])
def ask_chatbot():
    question = request.json.get('question')
    
    # Retrieve the stored text for processing
    response = query_rag(question)
    return jsonify({"response": response}), 200

if __name__ == '__main__':
    app.run(debug=True)