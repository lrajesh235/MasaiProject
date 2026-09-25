# Support Assistant Module README

## Overview
The Support Assistant module is designed to provide users with quick access to Zepto's policies through a conversational interface. This module utilizes a combination of document embedding, intent classification, and response generation to answer user queries effectively.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd zepto-ai-ml-capstone
   ```

2. **Install Dependencies**
   Navigate to the `support_assistant` directory and install the required packages:
   ```bash
   cd support_assistant
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 7860
   ```

4. **Access the API**
   The API will be available at `http://localhost:7860/ask`. You can send POST requests to this endpoint with your queries.

## Design Decisions
- **Document Ingestion**: The policy documents are loaded and embedded using the `ingest.py` script, which stores the embeddings in a ChromaDB collection for efficient retrieval.
- **Intent Classification**: The LangGraph StateGraph defined in `graph.py` routes user queries based on their intent, distinguishing between policy-related questions and general inquiries.
- **Response Generation**: The structured prompt templates in `prompts.py` ensure that responses are generated based on the retrieved context, maintaining relevance and accuracy.

## Example Queries
- For policy-related questions, such as "What is the delivery policy?", the system retrieves relevant information from the embedded documents.
- For general questions, such as "What are your business hours?", a fixed response is provided indicating the limitations of the assistant.

## Architecture
The Support Assistant follows a Retrieval-Augmented Generation (RAG) pipeline:
1. **Ingestion**: Documents are loaded and embedded.
2. **Embedding**: The embeddings are stored in ChromaDB.
3. **Retrieval**: User queries are processed to retrieve relevant document chunks.
4. **Generation**: Responses are generated based on the retrieved context.

This module is designed to operate in a mock mode by default, ensuring that no external API calls are made during grading.