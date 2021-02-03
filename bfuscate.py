#
# Created by @Joeylent on repl.it
#

import utils

import string
import random
import sys
import re



# List of all the types (I've found)
types = {
    "''":
    '',               # <class 'str'>

    "1":
    1,                # <class 'int'>

    "(not())":
    True,             # <class 'bool'>

    "(not().__len__())":
    False,

    "[]":
    [],               # <class 'list'>

    "()":
    (),               # <class 'tuple'>

    "{}":
    {},               # <class 'dict'>

    "(()for _ in())":
    (()for _ in()),   # <class 'generator'>

    "type":
    type,             # <class 'type'>

    "lambda:(()).__len__()":
    lambda:(()).\
    __len__(),        # <class 'function'>

    "len":
    len,              # <class 'builtin_function_or_method'>

    "help":
    help              # <class '_sitebuiltins._Helper'>
}


matches = {}



# Generate a table of existing characters within
# the types and their matches
for c in string.printable:
    l = []

    for t,v in types.items():
        if c in str(type(v)):
            l.append(t)

    if l: matches[c] = l



# Translate file
filename = sys.argv[sys.argv.index("-f") + 1]
output   = sys.argv[sys.argv.index("-o") + 1] if "-o" in sys.argv else filename.split(".")[0]+"_BFUSCATED.py"

## Read
with open(filename) as f:
    code = f.read().replace("\"", "'")

## Translate
translated = "exec(eval(open(__file__).read().split(chr((((),()).__len__()**((),()).__len__())*(((),()).__len__()+[()].__len__())*((),(),()).__len__()-[()].__len__()))[[()].__len__()]))#"
segments   = []

for c in code:
    ### Check if c has a match
    if c in matches:
        chosenType  = random.choice(matches[c])
        chosenIndex = random.choice(utils.find(c, str(type(eval(chosenType)))))
        splitIndex  = utils.split(chosenIndex)
        
        segments.append("str(type({}))[{}-{}]".format(
            chosenType,
            "*".join(
                "({}**{})".format(
                    "({}).__len__()".format("()," * n),
                    "({}).__len__()".format("()," * a)
                )
                for n,a in splitIndex[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * splitIndex[1])) if splitIndex[1] > 0 else "(()).__len__()"
        ))
    
    
    ### Check if c is uppercase and has lowercase counterpart
    elif c.isupper() and c.lower() in matches:
        chosenType  = random.choice(matches[c.lower()])
        chosenIndex = random.choice(utils.find(c.lower(), str(type(eval(chosenType)))))
        splitIndex  = utils.split(chosenIndex)
        
        segments.append("chr(ord(str(type({}))[{}-{}])-(((),()).__len__()**((),(),(),(),()).__len__()))".format(
            chosenType,
            "*".join(
               "({}**{})".format(
                   "({}).__len__()".format("()," * n),
                   "({}).__len__()".format("()," * a)
                )
                for n,a in splitIndex[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * splitIndex[1])) if splitIndex[1] > 0 else "(()).__len__()"
        ))


    ### Check if c is a digit
    elif c in string.digits:
        splitNum = utils.split(int(c))

        segments.append("str({}-{})".format(
            "*".join(
               "({})".format(
                   "*".join(["({}).__len__()".format("()," * n)] * a)
                )
               for n,a in splitNum[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * splitNum[1])) if splitNum[1] > 0 else "(()).__len__()"
        ))
    
    
    ### Create character
    else:
        splitNum = utils.split(ord(c))

        segments.append("chr({}-{})".format(
            "*".join(
               "({}**{})".format(
                   "({}).__len__()".format("()," * n),
                   "({}).__len__()".format("()," * a)
                )
               for n,a in splitNum[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * splitNum[1])) if splitNum[1] > 0 else "(()).__len__()"
        ))

translated += "+".join(segments)

## Write
with open(output, "w+") as f:
    f.write(translated)
