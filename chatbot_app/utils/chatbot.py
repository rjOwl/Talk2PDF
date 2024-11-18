from transformers import pipeline

# Load a pre-trained model for question answering
# qa_pipeline = pipeline("question-answering")

def get_response(question):
    # Here you would retrieve the context from the uploaded documents
    context = "..."  # Replace with actual context
    # result = qa_pipeline(question=question, context=context)
    # return result['answer']
    return [1,2,3]