import string
import random
import bfuscate.utils as utils
from bfuscate.constants import *


def lambda_bfuscate(character: chr) -> str:
    """
    Obfuscates a character using lambdas.
    """

    # Check if character has a match
    if character in matches:
        chosen_type = random.choice(matches[character])
        chosen_index = random.choice(utils.find(character, chosen_type["type"]))

        return "str({}.__class__)[{}]".format(
            chosen_type["get"](), utils.convert(chosen_index)
        )

    # Check if character is uppercase and has lowercase counterpart
    elif character.isupper() and character.lower() in matches:
        chosen_type = random.choice(matches[character.lower()])
        chosen_index = random.choice(utils.find(character.lower(), chosen_type["type"]))

        return "chr(ord(str({}.__class__)[{}])-(((),()).__len__()**((),(),(),(),()).__len__()))".format(
            chosen_type["get"](), utils.convert(chosen_index)
        )

    # Check if character is a digit
    elif character in string.digits:
        return "str({})".format(utils.convert(int(character)))

    # Create character
    else:
        return "chr({})".format(utils.convert(ord(character)))


def len_bfuscate(character: chr) -> str:
    """
    Obfuscates a character using len.
    """

    # Check if character has a match
    if character in matches:
        chosen_type = random.choice(matches[character])
        chosen_index = random.choice(utils.find(character, chosen_type["type"]))
        split_num = utils.split(chosen_index)

        return "str({}.__class__)[{}-{}]".format(
            chosen_type["get"](),
            "*".join(
                "({}**{})".format(
                    "({}).__len__()".format("()," * n),
                    "({}).__len__()".format("()," * a),
                )
                for n, a in split_num[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * split_num[1]))
            if split_num[1] > 0
            else "(()).__len__()",
        )

    # Check if character is uppercase and has lowercase counterpart
    elif character.isupper() and character.lower() in matches:
        chosen_type = random.choice(matches[character.lower()])
        chosen_index = random.choice(utils.find(character.lower(), chosen_type["type"]))
        split_num = utils.split(chosen_index)

        return "chr(ord(str(type({}))[{}-{}])-(((),()).__len__()**((),(),(),(),()).__len__()))".format(
            chosen_type["get"](),
            "*".join(
                "({}**{})".format(
                    "({}).__len__()".format("()," * n),
                    "({}).__len__()".format("()," * a),
                )
                for n, a in split_num[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * split_num[1]))
            if split_num[1] > 0
            else "(()).__len__()",
        )

    # Check if character is a digit
    elif character in string.digits:
        split_num = utils.split(int(character))

        return "str({}-{})".format(
            "*".join(
                "({})".format("*".join(["({}).__len__()".format("()," * n)] * a))
                for n, a in split_num[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * split_num[1]))
            if split_num[1] > 0
            else "(()).__len__()",
        )

    # Create character
    else:
        split_num = utils.split(ord(character))

        return "chr({}-{})".format(
            "*".join(
                "({}**{})".format(
                    "({}).__len__()".format("()," * n),
                    "({}).__len__()".format("()," * a),
                )
                for n, a in split_num[0].items()
            ),
            "({}).__len__()".format(",".join(["()"] * split_num[1]))
            if split_num[1] > 0
            else "(()).__len__()",
        )
