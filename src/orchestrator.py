import os
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.sql_agent import ask_sql
from agents.rag_agent import ask_rag

from config import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


SYSTEM_PROMPT = """
You are an intelligent routing agent.

Classify the user query.

If it asks about:

- Patients
- Doctors
- Hospitals
- Billing
- Insurance
- Medicines
- Blood groups
- Diseases
- Admission
- Discharge
- Medical statistics

Return ONLY

SQL

If it asks about

- Hospital policy
- Visitor rules
- Emergency procedures
- Insurance policy
- Privacy policy
- Staff policy
- Fire safety
- ICU rules
- Documents

Return ONLY

RAG

Do not explain.
"""


def classify(question):

    prompt = SYSTEM_PROMPT + "\n\nQuestion:\n" + question

    result = llm.invoke(prompt)

    return result.content.strip().upper()


def route_query(question):

    agent = classify(question)

    print(f"Selected Agent : {agent}")

    if "SQL" in agent:

        return ask_sql(question)

    return ask_rag(question)