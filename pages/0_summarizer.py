import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from ai import model

# prompt
system_template = "be a professional resume buliding consultant for a software engineer. Extract keywords from this job description to help me select relevant technical projects and hard skills. Your output will be JSON format and succinct"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)


# user input
job_description = st.text_area("Job description", placeholder="Paste description here", height=300, key="main")

if st.button("Summarize and save"):
    if job_description:
        prompt = prompt_template.invoke({"text": job_description}) 

        response = model.invoke(prompt)
        output_text = response.content   # JSON format now
        st.session_state.job_description_keywords = output_text
    else:
        st.warning("Please enter some text first")


# Output

if "job_description_keywords" not in st.session_state:
    st.session_state.job_description_keywords = None

if st.session_state.job_description_keywords:
    st.write(st.session_state.job_description_keywords)
