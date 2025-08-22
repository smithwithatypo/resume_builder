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
system_template = "be a helpful assistant. summarize in one sentence."

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)


user_text = st.text_area("text here", placeholder="Paste text here", height=300)

if st.button("Generate response"):
    if user_text:
        prompt = prompt_template.invoke({"text": user_text}) 

        response = model.invoke(prompt)
        output_text = response.content

        st.write(output_text)
    else:
        st.warning("Please enter some text first")

