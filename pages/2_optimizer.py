import streamlit as st
from ai import model
from data.projects import all_projects 
from langchain_core.prompts import ChatPromptTemplate
from util.format_for_llm import format_projects_for_llm


# run Summarizer first to populate session_state
if "job_description_keywords" in st.session_state:
    job_keywords = st.session_state.job_description_keywords
    projects_string = format_projects_for_llm(all_projects)
    
    # Enhanced prompt for semantic matching
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an expert resume consultant specializing in semantic matching between job requirements and project experience.

Your task: Analyze the provided projects and rank them by relevance to the job requirements.

Consider:
1. Keyword matches (exact and semantic)
2. Technical skills alignment
3. Domain/industry relevance
4. Impact and scale indicators
5. Technology stack overlap

Output format:
1. List the top 3-5 most relevant projects
2. For each project, explain why it's relevant
3. Highlight specific keywords/skills that match
4. Suggest any modifications to emphasize relevance"""),
        
        ("user", """Job Requirements Analysis:
{job_keywords}

Available Projects:
{projects}

Please rank and analyze the most relevant projects for this role.""")
    ])
    
    prompt = prompt_template.invoke({
        "job_keywords": job_keywords,
        "projects": projects_string
    })
    
    if st.button("run model"):
        response = model.invoke(prompt)
        st.header("job keywords")
        st.write(job_keywords)

        st.header("projects string")
        st.write(projects_string)
        
        st.header("ai response")
        st.write(response.content)
else:
    st.warning("Please enter a job description on the Summarizer page first")
