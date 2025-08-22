import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from data.skills import skills


# config
load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")


# prompt
# system_template = str(me.items())
system_template = "be a helpful assistant"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)


# input
user_text = "give me life advice.  summarize in 1 sentence"
prompt = prompt_template.invoke({"text": user_text}) 


# output
response = model.invoke(prompt)
output_text = response.content

# print("wrote response to output.txt")
print("output with print: ", output_text)
st.write("output with st.write: ", output_text)
st.write("skills are", skills)