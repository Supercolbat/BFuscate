import string
import random
import utils


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
