from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_function():
    # Use a pre-trained Hugging Face model for embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
