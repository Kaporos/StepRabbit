from typing import List


import dateutil.parser
import datetime


# custom Decoder
def DecodeDateTime(empDict):
    if "joindate" in empDict:
        empDict["joindate"] = dateutil.parser.parse(empDict["joindate"])
        return empDict


class Step:
    def __init__(self, json_step: dict):
        self.name: str = json_step["name"]
        self.inputs: List[str] = json_step["inputs"]
        self.outputs: List[str] = json_step["outputs"]
        self.worker_type: str = json_step["worker_type"]

    def toJson(self) -> dict:
        return {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "worker_type": self.worker_type,
        }


class Script:
    def __init__(self, json_script: dict):
        self.steps: List[Step] = []
        for step in json_script:
            self.steps.append(Step(step))

    def toJson(self) -> list:
        json_steps: List[dict] = []
        for step in self.steps:
            json_steps.append(step.toJson())
        return json_steps


class Execution:
    def __init__(self, id: int = 0, status: str = "success"):
        self.datetime = datetime.datetime.now()
        self.status = status

    def fromJson(self, jsonExec):
        self.id = jsonExec["id"]
        self.datetime = jsonExec["datetime"]
        self.status = jsonExec["status"]


class Program:
    def __init__(self, json_program: dict):
        self.name: str = json_program["name"]
        self.executions: List[Execution] = []
        self.script: Script = Script(json_program["script"])

    def toJson(self) -> dict:
        return {"name": self.name, "script": self.script.toJson()}
