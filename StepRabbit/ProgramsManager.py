import os,json
class ProgramsManager:
    def __init__(self,programs_directory):
        self.programs_directory = programs_directory
        self.programs = []
        self.reload()
    def reload(self):
        for entry in os.listdir(self.programs_directory):
            if os.path.isfile(os.path.join(self.programs_directory, entry)):
                with open(os.path.join(self.programs_directory, entry)) as f:
                  data = json.load(f)
                  self.programs.append({"name":data["name"],"script":data["script"]})
    def get_programs(self):
        return self.programs
    def get_programs_by_name(self):
        programs = {}
        index = 0
        for program in self.programs:
            programs[program["name"]] = self.programs[index]
            index += 1
        return programs
    def get_programs_by_id(self):
        programs = {}
        index = 0
        for program in self.programs:
            programs[index] = program["name"]
            index += 1
        return programs
