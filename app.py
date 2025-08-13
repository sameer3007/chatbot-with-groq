#importing all the environment variables
import os
from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()


#importing streamlit for building the web app
import streamlit as st


#from langchain_core import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


#Output parser for string responses
from langchain_core.output_parsers import StrOutputParser


#------------------------------------------------------------------------------------------------
# This line sets the LANGSMITH project environment variable for tracking and debuging the project
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
# Setting the environment variable for the LANGSMITH API key
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
# Setting the environment variable for LangChain tracking
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")
# This is the endpoint for LangSmith tracing
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# This is GROQ api key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
#------------------------------------------------------------------------------------------------

# Initialize the model
from langchain_groq import ChatGroq
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)
def generate_response(question):
    llm=model
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Q&A Chatbot With ChatGroq By Sameer")

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")


if user_input :
    response=generate_response(user_input)
    st.write(response)
else:
    st.write("Please provide the user input")



