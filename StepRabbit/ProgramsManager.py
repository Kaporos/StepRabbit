import os, json
from typing import List
from StepRabbit.Program import Program
from StepRabbit.Caller import Caller


class ProgramsManager:
    def __init__(self, host: str, programs_directory: str):
        self.programs_directory = programs_directory
        self.programs: List[Program] = []
        self.caller = Caller(host)
        self.reload()

    def reload(self):
        self.programs = []
        for entry in os.listdir(self.programs_directory):
            if os.path.isfile(os.path.join(self.programs_directory, entry)):
                with open(os.path.join(self.programs_directory, entry)) as f:
                    data = json.load(f)
                    print("DETECTED : " + json.dumps(data))

                    program = Program(data)
                    self.programs.append(program)

    def get_programs(self) -> list:
        return self.programs

    def get_program_by_name(self, name: str) -> Program:
        index = 0
        for program in self.programs:
            if program.name == name:
                return self.programs[index]
        raise KeyError("Il n'existe aucun programme de ce nom")

    def get_program_by_id(self, id: int) -> Program:
        if len(self.programs) > id:
            return self.programs[id]
        raise IndexError("Il n'existe aucun programme possédant cet id")

    def run(self, program: Program, args: dict) -> dict:
        return self.caller.execute(program, args)

    def toJson(self) -> list:
        json_list = []
        id = 0
        for program in self.programs:
            json_prog = program.toJson()
            json_prog["id"] = id
            json_list.append(json_prog)
            id += 1
        return json_list
