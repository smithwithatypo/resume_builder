
class ProjectClass:
    def __init__(self, title, keywords=None, bulletpoints=None):
        self.title = title
        self.keywords = set(keywords) if keywords else set()
        # self.bulletpoint_list = bulletpoints or []
        self.bulletpoints = set(bulletpoints) if bulletpoints else set()