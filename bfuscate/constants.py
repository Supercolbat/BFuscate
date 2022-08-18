"""
Messiest file as of yet.
"""

import string
import random

import bfuscate.utils as utils

# Define the types
TYPES = {
    # <class 'str'>
    "str": {"get": lambda: '""', "type": str(str)},
    # <class 'int'>
    "int": {
        "get": lambda: "(([{2}]{0}[{3}]){6}([{4}]{1}[{5}]))".format(
            ">" if random.randint(0, 1) else "<",
            ">" if random.randint(0, 1) else "<",
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            "+" if random.randint(0, 1) else "-",
        ),
        "type": str(int),
    },
    # <class 'float'>
    "float": {"get": lambda: str(random.random()), "type": str(float)},
    # <class 'bool'>
    "bool": {
        "get": lambda: random.choice(
            [
                "({}>{})".format(
                    utils.convert(random.randint(1, 10)),
                    utils.convert(random.randint(1, 10)),
                ),
                "(not({}).__len__())".format(",".join(["()"] * random.randint(1, 10))),
            ]
        ),
        "type": str(bool),
    },
    # <class 'list'>
    "list": {"get": lambda: "[]", "type": str(list)},
    # <class 'tuple'>
    "tuple": {"get": lambda: "()", "type": str(tuple)},
    # <class 'dict'>
    "dict": {"get": lambda: "{}", "type": str(dict)},
    # <class 'generator'>
    "generator": {"get": lambda: "(()for _ in())", "type": str(type((() for _ in ())))},
    # <class 'type'>
    "type": {
        "get": lambda: random.choice(["type", "str", "int", "float"]),
        "type": str(type),
    },
    # <class 'function'>
    "function": {"get": lambda: "(lambda:())", "type": str(type(lambda: ()))},
    # <class 'builtin_function_or_method'>
    "builtin_function_or_method": {
        "get": lambda: random.choice(["len", "print", "input"]),
        "type": str(type(len)),
    },
    # <class '_sitebuiltins._Helper'>
    "_sitebuiltins._Helper": {"get": lambda: "help", "type": str(type(help))},
}
HEADER = "exec(eval(open(__file__).read().split(chr((((),()).__len__()**((),()).__len__())*(((),()).__len__()+[()].__len__())*((),(),()).__len__()-[()].__len__()))[[()].__len__()]))#"

# Generate a dict of existing characters within
# the types and their matches
matches = {}
for letter in string.printable:
    characters = [element for element in TYPES.values() if letter in element["type"]]

    if characters:
        matches[letter] = characters
