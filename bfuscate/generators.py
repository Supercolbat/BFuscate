import random
import string
import time

class VariableNameGenerator:
    def __init__(self):
        self.methods = (
            self.l_and_I,
            self.O_and_0,
        )
        self.generated_names = []

    def l_and_I(self, length: int = 8) -> str:
        name = "".join(random.choices("lI", k=length))
        if name in self.generated_names:
            name = self.l_and_I(length)

        self.generated_names.append(name)
        return name
    
    def O_and_0(self, length: int = 8) -> str:
        name = "O" + "".join(random.choices("O0", k=length))
        if name in self.generated_names:
            name = self.l_and_I(length)
        
        self.generated_names.append(name)
        return name