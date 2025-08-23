import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from ai import model

# prompt
system_template = "be a professional resume buliding consultant for a software engineer. be succinct."


prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)

result = ""
metric = ""
action = ""
explanation = ""

radio_options = {
    0: {
        "title": "Complete bullet point",
        "prompt": "give me a great resume bullet point if my result is {result}, my metric is {metric}, my action is {action}"
    },
    1: {
        "title": "Sections from my explanation",
        "prompt": "please extract a Result (like impact on user or developers), Metric (measurable impact of the result), Action (specific action I took), and some keywords that would match ATS from this explanation of what I did: {explanation}"
    },
}

generation_option = st.radio(
    "What would you like to generate?",
    [radio_options[0]["title"], radio_options[1]["title"]]
)


if generation_option == radio_options[0]["title"]:
    result = st.text_area("result", placeholder="achieved X", height=100, key=0)
    metric = st.text_area("metric", placeholder="as measured by Y", height=100, key=1)
    action = st.text_area("action", placeholder="by doing Z", height=100, key=2)
elif generation_option == radio_options[1]["title"]:
    explanation = st.text_area("explanation", placeholder="explain what you did", height=200, key=3)


if st.button("Generate response"):
    # print("button pressed")
    if result or metric or action or explanation:
        if generation_option == radio_options[0]["title"]:
            user_input = radio_options[0]["prompt"].format(result=result, metric=metric, action=action)
        elif generation_option == radio_options[1]["title"]:
            user_input = radio_options[1]["prompt"].format(explanation=explanation)
        
        prompt = prompt_template.invoke({"text": user_input}) 
        print("about to call ai")
        response = model.invoke(prompt)
        print("finished calling ai")
        output_text = response.content

        st.write(output_text)
        with st.expander("📋 Copy text easier here"):
            st.code(output_text, language=None)
    else:
        st.warning("Please enter some text")

