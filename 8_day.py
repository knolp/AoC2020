class Command():
    def __init__(self, text):
        self.type, self.value = text.split(" ")
        self.value = int(self.value)
        self.ran = False
        self.modified = False
        self.moddable = False
        if self.type in ["nop", "jmp"]:
            self.moddable = True

    def execute(self):
        self.ran = True

        if self.type == "nop":
            return 0, 1
        
        if self.type == "jmp":
            return 0, self.value
        
        if self.type == "acc":
            return self.value, 1

    def modify(self):
        if self.moddable:
            self.modified = True
            if self.type == "nop":
                self.type = "jmp"
            else:
                self.type = "nop"
        else:
            return

    def de_modify(self):
        if self.moddable:
            self.modified = False
            if self.type == "nop":
                self.type = "jmp"
            else:
                self.type = "nop"
        else:
            return


        


class Assembler():
    def __init__(self, instr):
        with open(instr) as f:
            self.instructions = [Command(x) for x in f.read().split("\n")]
        
        self.tried = []
        self.mod_instructions()

        self.accumulator = 0
        self.mod_i = 0
    
    def run(self):
        i = 0
        done = False
        while True:
            if i >= len(self.instructions):
                break
            if not self.instructions[i].ran:
                acc, plus = self.instructions[i].execute()
                self.accumulator += acc
                i += plus
            else:
                self.accumulator = 0
                i = 0
                self.mod_instructions()
                continue

        return self.accumulator

    def mod_instructions(self):
        for i in range(len(self.instructions)):
            self.instructions[i].ran = False
        for i in range(len(self.instructions)):
            if self.instructions[i].modified:
                self.instructions[i].de_modify()
            if self.instructions[i].moddable and i not in self.tried:
                self.tried.append(i)
                self.instructions[i].modify()
                break





if __name__ == "__main__":
    machine = Assembler("input8.txt")
    print(machine.run())
