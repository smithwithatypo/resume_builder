import streamlit as st
from data.projects import all_projects 


# search = "ux"
# for x in data.projects.dell_2024.bulletpoint_list:
#     st.write(x.keywords)

#     if search in x.keywords:
#         st.write("yes", search)
#     else:
#         st.write("no", search)



if "job_description_keywords" in st.session_state:
    data = st.session_state.job_description_keywords
    st.write("data loaded: ", len(data))

for project in all_projects:
    print( (project.keywords, project.id) )
