from .RabbitClient import RabbitClient
from .Classes import *
import json
class Caller:
    def __init__(self,host):
        self.rabbit = RabbitClient(host)
    def execute_script(self,script,args):
        self.run(script,args)
    def execute_string_script(self,script,args):
        self.run(json.loads(script),args)
    def execute(self,program,args):
        print("Executing : "+program["name"])
        self.run(program["script"],args)
    def interactive_execute_script(self,script):
        self.run(script)
    def interactive_execute_string_script(self,script):
        self.run(json.loads(script))
    def interactive_execute(self,program):
        print("Executing : "+program["name"])
        self.run(program["script"])

    def run(self,script,vars={}):
        debugger = Debugger()
        step_index = Index()

        for json_step in script:
            step = Step(json_step)
            exec_vars = []

            Debugger.debug(str(step_index.value)+" -----> "+step.name)

            for input_name in step.inputs:
                if not input_name in vars.keys():
                    value = input(input_name+"  > ")
                    vars[input_name] = value
                    exec_vars.append(value)
                else:
                    exec_vars.append(vars[input_name])

            response = self.rabbit.call(exec_vars,step.worker_adress)
            Debugger.debug(response)
            index = Index()
            for output_name in step.outputs:
                    vars[output_name] = response[index.value]
                    index.value += 1
            step_index.value += 1
        return vars
