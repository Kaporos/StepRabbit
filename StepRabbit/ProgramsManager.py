import os, json
from typing import List
from StepRabbit.Program import Program


class ProgramsManager:
    def __init__(self, programs_directory: str):
        self.programs_directory = programs_directory
        self.programs: List[Program] = []
        self.reload()

    def reload(self):
        for entry in os.listdir(self.programs_directory):
            if os.path.isfile(os.path.join(self.programs_directory, entry)):
                with open(os.path.join(self.programs_directory, entry)) as f:
                    data = json.load(f)
                    self.programs.append(Program(data))

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
