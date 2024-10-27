# DocuMate 📄🤖

DocuMate is a Streamlit-based application designed to provide intelligent document search and question-answering capabilities using vector embeddings and large language models (LLMs). With DocuMate, users can upload PDF files, which the app then processes to answer questions based on document content.

## Features
- **PDF Uploads**: Upload multiple PDF documents for analysis.
- **Document Splitting**: Splits documents into chunks for efficient processing.
- **Vector Embeddings**: Generates embeddings for fast document retrieval.
- **Question Answering**: Provides accurate answers to user questions based on document content.
- **Document Similarity Search**: Retrieves similar document chunks based on context.

## Prerequisites
Before running the project, make sure to have the following installed:
- Python 3.7+
- Streamlit

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/DocuMate.git
   cd DocuMate
Usage
Run the Streamlit App:

bash
Copy code
streamlit run app.py
Upload PDF Files:

Use the file uploader in the app to upload PDF files for analysis.
Ask Questions:

Enter questions related to the document content in the text input box.
Click the "Submit" button to generate answers based on document content.
Document Similarity Search:

Access similar document chunks within the "Document Similarity Search" expander.
Project Structure
bash
Copy code
├── app.py                 # Main application file
├── README.md              # Documentation for GitHub
├── requirements.txt       # List of required packages
└── ...
Technologies Used
Streamlit: Frontend interface
LangChain: LLM-based framework for document chaining and retrieval
FAISS: Vector store for efficient document retrieval
PyPDFLoader: PDF document loading and processing
Troubleshooting
No PDF Documents Loaded: Ensure uploaded files are in PDF format.
Vector Store Not Initialized: Click the "Submit" button after uploading PDF files to initialize vector embeddings.
Contributing
If you want to contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Create a pull request.
License
This project is licensed under the MIT License. See LICENSE for details.

Acknowledgments
Special thanks to the LangChain, FAISS, and Streamlit communities for their support and libraries, which made this project possible.

