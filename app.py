import streamlit as st
import os
import time
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# Set your API keys
groq_api_key = "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"
google_api_key = "AIzaSyAOWJGZ7YsJxefdaNzQK8RSfGxExBBa4g0"

os.environ["GOOGLE_API_KEY"] = google_api_key

st.title("Welcome to DocuMate")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}
    """
)

def vector_embedding(uploaded_files):
    if "vectors" not in st.session_state:
        model_name = "models/embedding-001"
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model=model_name)  # Embedding Model
        
        docs = []
        for file in uploaded_files:
            if file.type == "application/pdf":
                # Save the uploaded file temporarily
                with open(file.name, "wb") as f:
                    f.write(file.getbuffer())
                
                # Load the PDF file using PyPDFLoader
                pdf_loader = PyPDFLoader(file.name)  # Load PDF documents from the file path
                docs.extend(pdf_loader.load())  # Load PDF documents
                
                # Optionally, delete the temporary file after loading
                os.remove(file.name)
            else:
                st.warning(f"{file.name} is not a PDF file. Please upload PDF files only.")

        if not docs:
            st.error("No PDF documents loaded. Please check the files.")
            return
        
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # Chunk Creation
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(docs)  # Splitting
        
        if not st.session_state.final_documents:
            st.error("No documents after splitting. Please check the document content.")
            return
        
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)  # Vector OpenAI embeddings
        st.success("Now we are ready to answer your questions!!")

# Input for user question
prompt1 = st.text_input("Ask me your questions!!")

# File uploader for PDF files
uploaded_files = st.file_uploader("Upload your PDF files", type='pdf', accept_multiple_files=True)

# Button to trigger vector embedding
if st.button("Submit"):
    if uploaded_files:
        vector_embedding(uploaded_files)
    else:
        st.error("Please upload PDF files before clicking the button.")

if prompt1:
    # Check if vectors are initialized before accessing
    if "vectors" not in st.session_state:
        st.error("Vector store not initialized. Please click 'Click me first👾' after uploading PDF files.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        start = time.process_time()
        response = retrieval_chain.invoke({'input': prompt1})
        st.write("Response time:", time.process_time() - start)
        st.write(response['answer'])

        # With a streamlit expander for document similarity search
        with st.expander("Document Similarity Search"):
            # Find the relevant chunks
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("--------------------------------")