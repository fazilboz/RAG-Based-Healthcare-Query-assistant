# RAG-Based-Healthcare-Query-assistant

## About the Project

The RAG-Based Healthcare Query Assistant is a simple AI-powered application developed to help hospital staff access healthcare information quickly using natural language.

Instead of searching through patient records or hospital policy documents manually, users can simply ask questions in plain English. The system automatically decides whether the question should be answered from the patient database or from hospital policy documents.

This project combines SQL, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to provide accurate and relevant responses through a single chat interface.

---

## Features

- Ask questions in natural language
- Retrieve patient information from a healthcare database
- Search hospital policy documents using RAG
- Automatic query routing using an Orchestrator Agent
- Simple and user-friendly Streamlit interface
- Powered by Google's Gemini API

---

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- SQLite
- FAISS
- Pandas

---

## Project Structure

```
Healthcare-RAG-Assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── agents/
├── database/
├── documents/
├── utils/
└── vectorstore/
```

---

## How to Run the Project

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Add your Gemini API key

Create a `.env` file and add:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

### 3. Create the database

```bash
python database/create_database.py
```

### 4. Build the vector database

```python
from agents.rag_agent import build_vector_database
build_vector_database()
```

### 5. Start the application

```bash
streamlit run app.py
```

---

## Sample Questions

### Patient Database

- Show all diabetic patients.
- How many patients are above 60 years old?
- Which doctor treated the most patients?
- What is the average billing amount?

### Hospital Policies

- What are the hospital visiting hours?
- Explain the insurance policy.
- What are the ICU visitor rules?
- What should staff do during an emergency?

---

## Future Improvements

Some features that can be added in future versions include:

- User authentication
- Conversation history
- Voice-based interaction
- Dashboard with hospital statistics
- Support for multiple hospitals

---

## Author

**Mohammed Fazil**

