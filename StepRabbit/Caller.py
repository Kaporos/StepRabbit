from StepRabbit.RabbitClient import RabbitClient
import json
from StepRabbit.Program import Program
from typing import *
from functools import lru_cache


class Caller:
    def __init__(self, host: str):
        self.rabbit = RabbitClient(host)

    def execute_script(self, program: dict, args):
        self.run(Program(program), args)

    def execute_string_script(self, program: str, args):
        self.run(Program(json.loads(program)), args)

    def execute(self, program: Program, args):
        print("Executing : " + program.name)
        self.run(program, args)

    @lru_cache(maxsize=0)
    def run(self, program: Program, in_vars) -> dict:
        vars = in_vars
        print("VARS : ")
        print(vars)
        step_index = 0

        for step in program.script.steps:
            exec_vars = {}

            print(str(step_index) + " -----> " + step.name)

            for input_name in step.inputs:
                if not input_name in vars.keys():
                    raise ValueError("Value of " + input_name + " not specified")
                else:
                    exec_vars[input_name] = vars[input_name]

            response = self.rabbit.call(exec_vars, step.worker_type)
            print(response)
            for output_name in step.outputs:
                vars[output_name] = response[output_name]
            step_index += 1

        return vars
