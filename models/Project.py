
class ProjectClass:
    def __init__(self, title, id=None, keywords=None, bulletpoints=None):
        self.id = id
        self.title = title
        self.keywords = set(keywords) if keywords else set()
        self.bulletpoints = set(bulletpoints) if bulletpoints else set()

    def __str__(self):
        bp_strings = [str(bp) for bp in self.bulletpoints]
        return f"Project(id={self.id}, title='{self.title}', keywords={list(self.keywords)}, bulletpoints={bp_strings})"
    
    def __repr__(self):
        return self.__str__()
