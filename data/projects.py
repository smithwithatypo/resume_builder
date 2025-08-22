from models.Project import ProjectClass
from models.BulletPoint import BulletPointClass


# Template for bullet points
'''
BulletPointClass(
    result="",
    metric="",
    action="",
    keywords=("ai", "llm", "python", "kubernetes", "docker", "automation")
),
'''

# Projects
dell_2024 = ProjectClass(
    title="AI-powered legal review automation",
    bulletpoints=[
        BulletPointClass(
            result="automated the legal review process of SOW contract negotiations for $2.4B global enterprise sales pipeline",
            metric="saved 7 hours of manual effort per week per sales agent",
            action="by researching viability, then developing and deploying an AI / NLP app with Python, Streamlit, and a large language model on an internal Kubernetes cluster",
            keywords=("ai", "llm", "python", "kubernetes", "docker", "automation")
        ),
        BulletPointClass(
            result="",
            metric="",
            action="",
            keywords=("ai", "llm", "python", "kubernetes", "docker", "automation")
        ),

    ]
)

dell_2023 = ProjectClass(
    title="",
    bulletpoints=[
        BulletPointClass(
            
        )
    ]
)