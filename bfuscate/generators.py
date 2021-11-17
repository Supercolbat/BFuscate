import random
import string
import time

class VariableNameGenerator:
    def __init__(self):
        self.methods = (
            self.l_and_I,
            self.O_and_0,
        )

    def l_and_I(self, length: int) -> str:
        return "".join(random.choices("lI", k=length - 1))
    
    def O_and_0(self, length: int) -> str:
        return "O" + "".join(random.choices("O0", k=length - 1))
