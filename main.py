import streamlit as st
from langchain_openai import  OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import FAISS 


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your Related to 2020-2024 jobs data 📈")

    agent = create_csv_agent(
            OpenAI(temperature=0), "./salaries.csv", verbose=True)

    user_question = st.text_input("Ask a question here and press enter: ")

    if user_question is not None and user_question != "":
        with st.spinner(text="In progress..."):
            st.write(agent.run(user_question))



if __name__ == "__main__":
    main()