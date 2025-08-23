
class BulletPointClass:
    def __init__(self, result, metric, action):
        self.result = result
        self.metric = metric
        self.action = action
        self.generated_bullet = f"{result} {metric} {action}"
    
    def __str__(self):
        return f"BulletPoint(result='{self.result}', metric='{self.metric}', action='{self.action}')"
    
    def __repr__(self):
        return self.__str__()