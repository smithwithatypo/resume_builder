from models.Project import ProjectClass
from models.BulletPoint import BulletPointClass

# export
all_projects = set()


# Template
'''
project_name = ProjectClass(
    id=1,
    title="",
    keywords=("ai", "llm", "python"),
    bulletpoints=[
        BulletPointClass(
            result="",
            metric="",
            action="",
            keywords=("ai", "llm", "python", "kubernetes", "docker", "automation")
        ),
    ]
)
all_projects.add(project_name)

'''


# Dell projects ##############################################################

dell_ai_automation = ProjectClass(
    id=1,
    title="AI automation",
    keywords=("ai", "llm", "python", "streamlit", "kubernetes", "docker"),
    bulletpoints=[
        BulletPointClass(
            result="automated legal review process of SOW contract negotiations for $2.4B enterprise sales pipeline",
            metric="saved 7 hours/week/salesperson",
            action="by designing, developing, and deploying an AI / NLP app on an internal Kubernetes cluster.",
        ),

    ]
)
all_projects.add(dell_ai_automation)

dell_survey_analysis = ProjectClass(
    id=2,
    title="Survey analysis",
    keywords=("nlp", "ux", "python"),
    bulletpoints=[
        BulletPointClass(
            result="Business and developers improved user experience through app enhancements (auto-population features and increased speed)",
            metric="80 enterprise sales agent surveys analyzed",
            action="Analyzed unstructured survey data from internal app using NLP and manual review",
        ),
    ]
)
all_projects.add(dell_survey_analysis)


dell_order_lookup = ProjectClass(
    id=3,
    title="",
    keywords=("full stack development", "angular", "node.js", "sql", "nosql", "process optimization", "sre", "pivotal cloud foundry"),
    bulletpoints=[
        BulletPointClass(
            result="Reduced order support resolution time by 12 hours per week per person globally",
            metric="12 hours/week/person time savings across global support teams",
            action="Developed a full-stack order lookup feature combining 7 queries in several different databases into a unified search interface for LATAM orders blocked by nuanced compliance issues",
        ),
    ]
)
all_projects.add(dell_order_lookup)

dell_python_script = ProjectClass(
    id=4,
    title="database reconciliation",
    keywords=("python", "database syncronization", "process automation", "sre", "http api"),
    bulletpoints=[
        BulletPointClass(
            result="Automated database synchronization process, eliminating manual data validation work",
            metric="Saved 5 hours per week of manual effort",
            action="Developed and deployed a Python automation script that monitors database discrepancies and triggers automatic updates via internal API calls",
        ),
    ]
)
all_projects.add(dell_python_script)

dell_etl = ProjectClass(
    id=23,
    title="ETL Tests",
    keywords=("etl", "data lake", "C# .NET", "Kafka", "sql", "nosql", "json", "big data", "elasticsearch", "stream processing"),
    bulletpoints=[
        BulletPointClass(
            result="Enabled transition from legacy batch-processing ETL to real-time streaming architecture for 300M customer record datalake",
            metric="eliminated a 5-minute batch processing window for 300M customer records",
            action="Developed tests for an ETL pipeline migration, validated SQL/NoSQL data models, and implemented testing framework for C# .NET solution with Kafka queue integration",
        ),
    ]
)
all_projects.add(dell_etl)


dell_hackathon = ProjectClass(
    id=5,
    title="automate team matching process",
    keywords=("hackathon", "process automation", "data modeling", "backend development", "python", "object oriented programming"),
    bulletpoints=[
        BulletPointClass(
            result="Won first place in company-wide hackathon among all Dell interns",
            metric="1st place",
            action="Designed and implemented an automated matching system replacing manual new-hire to manager assignment process using survey data and algorithmic optimization",
        ),
    ]
)
all_projects.add(dell_hackathon)





# Research projects ##########################################################

research_aita = ProjectClass(
    id=6,
    title="AI computer science tutor",
    keywords=("ai", "llm", "angular", "node.js", "full-stack development", "agile", "ci / cd"),
    bulletpoints=[
        BulletPointClass(
            result="secured $10,000 research funding and delivered a full-stack AI tutoring platform",
            metric=r"served 200 CS students across multiple courses, achieving over 90% user satisfaction based on 40 pages of qualitative feedback analysis",
            action="built an AI tutoring app using Angular, Node.js, PostgreSQL, and OpenAI API",
        ),
        BulletPointClass(
            result="deployed MVP to 200 students by our academic deadline while keeping additional features as future development tracks",
            metric="200 students used it",
            action="Architected modular system design with agile CI/CD pipelines that isolated the core tutoring engine from stakeholders' requested add-on features (anti-cheat, teacher analytics)",
        ),
    ]
)
all_projects.add(research_aita)


research_mow = ProjectClass(
    id=7,
    title="Mobile app for Meals on Wheels",
    keywords=("react native", "django", "python", "full-stack development", "agile", "git", "leadership", "code reviews"),
    bulletpoints=[
        BulletPointClass(
            result="delivered user-facing features for elderly nutrition platform",
            metric="served 5000 seniors in central texas through a $5M federally-funded project",
            action="by coordinating and mentoring a cross-functional team of frontend and backend engineers",
        ),
        BulletPointClass(
            result="Improved code quality and team velocity",
            metric="by conducting 50+ code reviews",
            action="by implementing Agile project management, mentoring 2 engineers in Git workflows, and translating stakeholder requirements into technical specifications",
        ),
    ]
)
all_projects.add(research_mow)


research_imics = ProjectClass(
    id=8,
    title="medical computer vision",
    keywords=("ai", "deep learning", "python", "tensorflow", "machine learning", "automation", "distributed computing", "computer vision"),
    bulletpoints=[
        BulletPointClass(
            result="Automated a data augmentation pipeline for medical computer vision research",
            metric="",
            action="by building a distributed infrastructure across 8 GPUs training custom convolutional neural networks from scratch using Tensorflow",
        ),
    ]
)
all_projects.add(research_imics)


research_aquaponic = ProjectClass(
    id=9,
    title="aquaponic farm automation",
    keywords=("iot", "system architecture", "python", "distributed systems", "fault tolerance", "automation", "cloud", "reliability", "cross-functional collaboration", "risk analysis"),
    bulletpoints=[
        BulletPointClass(
            result="Eliminated single point of failure crashes that previously brought down entire farm",
            metric=r"Improved system reliability from 0% fault tolerance to resilient multi-node operation supporting 40+ plants and dozens of fish",
            action="Redesigned raspberry pi network architecture from daisy-chain to fault-tolerant client/server system",
        ),
        BulletPointClass(
            result="Identified high-risk subsystems and implemented targeted risk mitigations",
            metric="Co-authored peer-reviewed publication with graduate student",
            action="Published research on FMEA and Digital Twin methodologies for complex system risk analysis",
        ),
    ]
)
all_projects.add(research_aquaponic)



# Extracurricular projects ##########################################################

teaching_assistant = ProjectClass(
    id=10,
    title="",
    keywords=("ai", "llm", "python"),
    bulletpoints=[
        BulletPointClass(
            result="Enhanced student understanding of production-ready software development practices",
            metric="80 students across 2 semesters",
            action="Taught full-stack software engineering principles and conducted code reviews for student projects",
        ),
        BulletPointClass(
            result="Improved grading workflow and consistency",
            metric="by 60% (15+ hours per assignment cycle)",
            action="by developing an automated unit testing framework to grade assignments",
        ),
    ]
)
all_projects.add(teaching_assistant)

gdsc = ProjectClass(
    id=11,
    title="google club",
    keywords=("machine learning", "cloud computer", "leadership", "data-driven", "app development", "project management"),
    bulletpoints=[
        BulletPointClass(
            result="Founded and scaled a computer science club with Google",
            metric="grew from 0 to 400+ members within a year",
            action="by recruiting 10 officers and leading workshops in modern software skills like machine learning, cloud, app development, and interview prep",
        ),
        BulletPointClass(
            result="improved student retention and industry readiness",
            metric="as measured by positive survey sentiments after 40 events, 2 hackathons, a Google campus visit, and a freshman orientation with 300 attendees",
            action="by leading 40+ technical and social events events in a year",
        ),
    ]
)
all_projects.add(gdsc)

ieee = ProjectClass(
    id=12,
    title="ieee club",
    keywords=("leadership", "project management", "team management", "technical education"),
    bulletpoints=[
        BulletPointClass(
            result="boosted student engagement and education",
            metric="with 20-70 weekly attendees, 7 robotics teams, and increased organizational funds by 17% (from $6k to $7k)",
            action="by leading a team of 17 officers to create weekly technical, social, and fundraising events",
        ),
    ]
)
all_projects.add(ieee)


# Apple projects ##########################################################

fraud_investigator = ProjectClass(
    id=25,
    title="fraud investigator",
    keywords=("risk management", "data analysis", "process optimization", "quality assurance"),
    bulletpoints=[
        BulletPointClass(
            result="Mitigated financial risk to the company and customers",
            metric="saving $1 billion of damages annually",
            action=r"by actioning 50+ cases daily at over 99% accuracy and training all the teams of North America",
        ),
    ]
)
all_projects.add(fraud_investigator)

tribal_knowledge = ProjectClass(
    id=26,
    title="tribal knowledge",
    keywords=("process optimization", "risk mitigation", "cross-functional leadership", "project management"),
    bulletpoints=[
        BulletPointClass(
            result="Solved leadership's biggest struggle",
            metric="for 140 team members teaching 40 productivity optimizations",
            action="by creating a database of tribal knowledge while mitigating the risk of this data being useful to any criminals who might gain access to it",
        ),
    ]
)
all_projects.add(tribal_knowledge)

apple_leadership = ProjectClass(
    id=27,
    title="program manager at apple",
    keywords=("program management", "cross-functional collaboration", "process optimization", "stakeholder engagement"),
    bulletpoints=[
        BulletPointClass(
            result="improved employee engagement and corporate giving",
            metric="engaging 1200+ unique employees",
            action="by organizing 250 community service events across 3 years",
        ),
    ]
)
all_projects.add(apple_leadership)








# Personal projects ##########################################################

french_with_ai = ProjectClass(
    id=14,
    title="french with ai",
    keywords=("ai", "Full-stack development", "Golang", "react", "ci/cd pipeline"),
    bulletpoints=[
        BulletPointClass(
            result="improved the experience of learning French",
            metric="by saving an average 20 minutes of lookup time per 1 hour of studying",
            action="by developing a full-stack AI-powered app using Go, React, generative AI, and Docker with an automated CI/CD pipeline deployment on Railway",
        ),
    ]
)
all_projects.add(french_with_ai)

learn_docker = ProjectClass(
    id=16,
    title="learn docker",
    keywords=("docker", "database", "container orchestration"),
    bulletpoints=[
        BulletPointClass(
            result="learned nuanced Docker networking and security",
            metric="reducing risk of bringing down production by 100%",
            action="by developing a Docker playground environment with multi-container architecture including frontend, backend, database services, and environment variables",
        ),
    ]
)
all_projects.add(learn_docker)

computersmyth = ProjectClass(
    id=17,
    title="computersmyth",
    keywords=("Web Development", "Open Source", "mentoring"),
    bulletpoints=[
        BulletPointClass(
            result="Increased access to computer science resources",
            metric="of 10+ apps, coding templates, and tutorials for full-stack software development",
            action="by creating a web platform for developers to freely access everything I've published",
        ),
    ]
)
all_projects.add(computersmyth)

resume_builder = ProjectClass(
    id=18,
    title="",
    keywords=("ai", "llm", "python", "streamlit"),
    bulletpoints=[
        BulletPointClass(
            result="reduced the time it takes to customize resumes for each job opening",
            metric="by 2+ hours per application",
            action="by coding a full-stack app that uses large language models to synthesize keywords from the job description, then references a list of all my projects with keywords, then ranks which projects are most relevant to this specific position",
        ),
    ]
)
all_projects.add(resume_builder)

# algo_training = ProjectClass(
#     id=19,
#     title="",
#     keywords=("ai", "llm", "python"),
#     bulletpoints=[
#         BulletPointClass(
#             result="",
#             metric="",
#             action="",
#         ),
#     ]
# )
# all_projects.add(algo_training)

python_algo_snippets = ProjectClass(
    id=20,
    title="python algorithm snippets",
    keywords=("python", "angular", "algorithms", "data structures"),
    bulletpoints=[
        BulletPointClass(
            result="Reduced the study time of advanced data structures and algorithms",
            metric="by 20% (estimated)",
            action="by developing and deploying an app that collects the most useful Python code snippets and makes them easily searchable using a filter and keywords.",
        ),
    ]
)
all_projects.add(python_algo_snippets)

txst_cs_student_guide = ProjectClass(
    id=21,
    title="txst cs student guide",
    keywords=("angular", "react", "education", "web development"),
    bulletpoints=[
        BulletPointClass(
            result="Increased access to educational resources to underprivileged students",
            metric="engaging 100+ CS students at my university",
            action="by developing an app that linked to 40+ free online tools that upper-classmen, professors, and professionals found most useful in their success journeys",
        ),
    ]
)
all_projects.add(txst_cs_student_guide)

project_prioritizer = ProjectClass(
    id=22,
    title="project prioritizer",
    keywords=("angular", "prioritization", "process optimization"),
    bulletpoints=[
        BulletPointClass(
            result="Reduced decision fatigue and time-to-action for people with multiple competing projects",
            metric="",
            action="by coding a lightweight app that uses the Eisenhower Matrix to rank all your projects in order of highest priority and gives you a clear actionable step for each project",
        ),
    ]
)
all_projects.add(project_prioritizer)
