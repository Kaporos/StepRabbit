
class Debugger:
    def __init__(self):
        pass
    def debug(status):
        print(status)

class Step:
    def __init__(self,json_step):
        print(json_step)
        self.inputs = json_step["input"]
        self.outputs = json_step["output"]
        self.name = json_step["name"]
        self.worker_adress = json_step["worker_adress"]

class Index:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
