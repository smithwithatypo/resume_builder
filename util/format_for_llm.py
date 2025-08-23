def format_projects_for_llm(projects_set):
    """Format projects in a clean, LLM-friendly way"""
    
    formatted_projects = set()
    
    for project in projects_set:
        project_text = f"""
PROJECT: {project.title} (ID: {project.id})
KEYWORDS: {', '.join(project.keywords)}
BULLET POINTS:
"""
        for bp in project.bulletpoints:
            project_text += f"""
  • RESULT: {bp.result}
  • METRIC: {bp.metric}
  • ACTION: {bp.action}
  • KEYWORDS: {', '.join(bp.keywords)}
  ---
"""
        formatted_projects.add(project_text)
    
    return "\n" + "="*80 + "\n".join(formatted_projects)