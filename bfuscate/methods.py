"""
Obfuscation functions for BFuscate
By @JoeyLent on repl.it
"""

import string
import random
import utils


# Define the types
TYPES = {
    # <class 'str'>
    "str": {
        "get": lambda: '""',
        "type": str(str)
    },

    # <class 'int'>
    "int": {
        "get": lambda: "(([{2}]{0}[{3}]){6}([{4}]{1}[{5}]))".format(
            ">" if random.randint(0, 1) else "<",
            ">" if random.randint(0, 1) else "<",
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            ",".join(["[]"] * random.randint(1, 5)),
            "+" if random.randint(0, 1) else "-"
        ),
        "type": str(int)
    },

    # <class 'float'>
    "float": {
        "get": lambda: str(random.random()),
        "type": str(float)
    },

    # <class 'bool'>
    "bool": {
        "get": lambda: random.choice([
            "({}>{})".format(
                utils.convert(random.randint(1, 10)),
                utils.convert(random.randint(1, 10))
            ),
            "(not({}).__len__())".format(
                ",".join(["()"] * random.randint(1, 10))
            )
        ]),
        "type": str(bool)
    },

    # <class 'list'>
    "list": {
        "get": lambda: "[]",
        "type": str(list)
    },

    # <class 'tuple'>
    "tuple": {
        "get": lambda: "()",
        "type": str(tuple)
    },

    # <class 'dict'>
    "dict": {
        "get": lambda: "{}",
        "type": str(dict)
    },

    # <class 'generator'>
    "generator": {
        "get": lambda: "(()for _ in())",
        "type": str(type((() for _ in ())))
    },

    # <class 'type'>
    "type": {
        "get": lambda: random.choice(["type", "str", "int", "float"]),
        "type": str(type)
    },

    # <class 'function'>
    "function": {
        "get": lambda: "(lambda:())",
        "type": str(type(lambda: ()))
    },

    # <class 'builtin_function_or_method'>
    "builtin_function_or_method": {
        "get": lambda: random.choice(["len", "print", "input"]),
        "type": str(type(len))
    },

    # <class '_sitebuiltins._Helper'>
    "_sitebuiltins._Helper": {
        "get": lambda: "help",
        "type": str(type(help))
    },
}
HEADERS = {
    True: "exec(eval((lambda f=open(__file__).read().split(chr((((),()).__len__()**((),()).__len__())*(((),"
          "()).__len__()+[()].__len__())*((),(),()).__len__()-[()].__len__())):(lambda s=[chr(int(c, ((((),"
          ")>(()))+(((),())>((),)))**(((())<((),()))+(((),(),)>((),)))**((()<((),))+(((),())>()))))for c in[f[(((),"
          "())>())+(()<())][l*(((())<((),()))+(((),())>(()))):(l+(((())>(()))+((())<((),))))*(((())<((),()))+(((),"
          "())>(())))]for l in range(len(f[((((),)<(()))+(((),)>(())))])//((((),)>(()))+(((),)>(()))))]]:''.join(chr("
          "ord(a)^ord(b))for a,b in zip(s,f[(((())<((),()))+(()<((),())))]*-(-len(s)//len(f[((((),)>(()))+(()<((),"
          "())))])))))())()))# ",
    False: "exec(eval(open(__file__).read().split(chr((((),()).__len__()**((),()).__len__())*(((),()).__len__("
           ")+[()].__len__())*((),(),()).__len__()-[()].__len__()))[[()].__len__()]))# "
}

# Generate a dict of existing characters within
# the types and their matches
matches = {}
for letter in string.printable:
    characters = [element for element in TYPES.values() if letter in element["type"]]

    if characters:
        matches[letter] = characters


def lambda_bfuscate(code, args) -> str:
    """
    Obfuscates python code with the lambda method.
    """

    obfuscated = HEADERS[args.defend]
    segments = []

    for character in code:
        # Check if character has a match
        if character in matches:
            chosen_type = random.choice(matches[character])
            chosen_index = random.choice(utils.find(character, chosen_type["type"]))

            segments.append("str({}.__class__)[{}]".format(
                chosen_type["get"](),
                utils.convert(chosen_index)
            ))

        # Check if character is uppercase and has lowercase counterpart
        elif character.isupper() and character.lower() in matches:
            chosen_type = random.choice(matches[character.lower()])
            chosen_index = random.choice(utils.find(character.lower(), chosen_type["type"]))

            segments.append("chr(ord(str({}.__class__)[{}])-(((),()).__len__()**((),(),(),(),()).__len__()))".format(
                chosen_type["get"](),
                utils.convert(chosen_index)
            ))

        # Check if character is a digit
        elif character in string.digits:
            segments.append("str({})".format(
                utils.convert(int(character))
            ))

        # Create character
        else:
            segments.append("chr({})".format(
                utils.convert(ord(character))
            ))

    obfuscated += "+".join(segments)

    return utils.encrypt(obfuscated) if args.defend else obfuscated


def len_bfuscate(code, args) -> str:
    """
    Obfuscates python code with the len method.
    """

    obfuscated = HEADERS[args.defend]
    segments = []

    for character in code:
        # Check if character has a match
        if character in matches:
            chosen_type = random.choice(matches[character])
            chosen_index = random.choice(utils.find(character, chosen_type["type"]))
            split_num = utils.split(chosen_index)

            segments.append("str({}.__class__)[{}-{}]".format(
                chosen_type["get"](),
                "*".join(
                    "({}**{})".format(
                        "({}).__len__()".format("()," * n),
                        "({}).__len__()".format("()," * a)
                    )
                    for n, a in split_num[0].items()
                ),
                "({}).__len__()".format(",".join(["()"] * split_num[1])) if split_num[1] > 0 else "(()).__len__()"
            ))

        # Check if character is uppercase and has lowercase counterpart
        elif character.isupper() and character.lower() in matches:
            chosen_type = random.choice(matches[character.lower()])
            chosen_index = random.choice(utils.find(character.lower(), chosen_type["type"]))
            split_num = utils.split(chosen_index)

            segments.append("chr(ord(str(type({}))[{}-{}])-(((),()).__len__()**((),(),(),(),()).__len__()))".format(
                chosen_type["get"](),
                "*".join(
                    "({}**{})".format(
                        "({}).__len__()".format("()," * n),
                        "({}).__len__()".format("()," * a)
                    )
                    for n, a in split_num[0].items()
                ),
                "({}).__len__()".format(",".join(["()"] * split_num[1])) if split_num[1] > 0 else "(()).__len__()"
            ))

        # Check if character is a digit
        elif character in string.digits:
            split_num = utils.split(int(character))

            segments.append("str({}-{})".format(
                "*".join(
                    "({})".format(
                        "*".join(["({}).__len__()".format("()," * n)] * a)
                    )
                    for n, a in split_num[0].items()
                ),
                "({}).__len__()".format(",".join(["()"] * split_num[1])) if split_num[1] > 0 else "(()).__len__()"
            ))

        # Create character
        else:
            split_num = utils.split(ord(character))

            segments.append("chr({}-{})".format(
                "*".join(
                    "({}**{})".format(
                        "({}).__len__()".format("()," * n),
                        "({}).__len__()".format("()," * a)
                    )
                    for n, a in split_num[0].items()
                ),
                "({}).__len__()".format(",".join(["()"] * split_num[1])) if split_num[1] > 0 else "(()).__len__()"
            ))

    obfuscated += "+".join(segments)

    if args.defend:
        return utils.encrypt(obfuscated)
    else:
        return obfuscated
