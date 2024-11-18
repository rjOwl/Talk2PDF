# Chatbot App

This project consists of a frontend application built with React and a backend service.

## Objective
Implement the Python-based application that uses AI/ML techniques to create a chatbot capable
of answering user questions based on information extracted from PDF documents. The
application should enable users to upload documents and interact with the chatbot through
a simple, accessible interface.

## Project Structure

- **client/**: Contains the React frontend application.
- **chatbot_app/**: Contains the backend service.

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Building the Whole Project

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Build and run the project using Docker Compose:
   ```bash
   docker compose up --build
   ```

4. Access the client application at [http://localhost:3000](http://localhost:3000).

### Stopping the Project

- To stop the running containers, use:
    ```bash
   docker compose down
   ```

### Additional Information

Refer to the individual submodule README files for more specific instructions on each part of the project.