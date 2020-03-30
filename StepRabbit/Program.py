from typing import List


class Step:
    def __init__(self, json_step: dict):
        self.name: str = json_step["name"]
        self.inputs: List[str] = json_step["inputs"]
        self.outputs: List[str] = json_step["outputs"]
        self.worker_type: str = json_step["worker_type"]


class Script:
    def __init__(self, json_script: dict):
        self.steps: List[Step] = []
        for step in json_script:
            self.steps.append(Step(step))


class Program:
    def __init__(self, json_program: dict):
        self.name: str = json_program["name"]
        self.script: Script = Script(json_program["script"])
