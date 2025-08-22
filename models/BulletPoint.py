
class BulletPointClass:
    def __init__(self, result, metric, action, keywords=None):
        self.result = result
        self.metric = metric
        self.action = action
        self.keywords = set(keywords) if keywords else set()
        self.generated_bullet = f"{result} {metric} {action}"