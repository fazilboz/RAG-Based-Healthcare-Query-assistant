import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from config import DATABASE_PATH, GOOGLE_API_KEY
import os

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

engine = create_engine(f"sqlite:///{DATABASE_PATH}")
db = SQLDatabase(engine)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

chain = create_sql_query_chain(llm, db)


def execute_sql(sql):

    conn = sqlite3.connect(DATABASE_PATH)

    try:

        df = pd.read_sql_query(sql, conn)

        conn.close()

        return df

    except Exception as e:

        conn.close()

        return str(e)


def dataframe_to_text(df):

    if isinstance(df, str):
        return df

    if df.empty:
        return "No matching records found."

    return df.to_markdown(index=False)


def ask_sql(question):

    sql = chain.invoke(
        {
            "question": question
        }
    )

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    print("\nGenerated SQL\n")
    print(sql)

    result = execute_sql(sql)

    result_text = dataframe_to_text(result)

    prompt = f"""
You are a hospital data assistant.

User Question:
{question}

SQL Query:
{sql}

SQL Result:
{result_text}

Explain the result in professional English.

If multiple rows exist summarize them.

If there are statistics explain them.

Do not mention SQL.
"""

    response = llm.invoke(prompt)

    return response.content