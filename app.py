import streamlit as st

from agents.orchestrator import route_query

st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 RAG-Based Healthcare Query Assistant")

st.markdown(
"""
Ask anything about

• Patient Records

• Hospital Policies

using natural language.
"""
)

if "messages" not in st.session_state:

    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


question = st.chat_input("Ask your question...")


if question:

    st.session_state.messages.append(

        {
            "role":"user",
            "content":question
        }

    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            answer = route_query(question)

            st.markdown(answer)

    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":answer
        }

    )