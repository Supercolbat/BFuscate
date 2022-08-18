"""
Extra functions to further obfuscate the source
"""

import re
import random

# \([\t ]*(?:([a-zA-Z_][\w\d]*)(?:,[\t ]*([a-zA-Z_][\w\d]*)[\t ]*(?::[\t ]*\w+|=[\t ]\d)?)*)\)


def rename_variables(charset, code) -> str:
    """
    Likely to go unused but renames variables.
    """

    variable_regex = re.compile(r"\b([a-zA-Z_]\w*)\s*:?=(?!=)[\t ]*.")
    def_regex = re.compile(
        r"[\t ]*def ([a-zA-Z_]\w*)\((?:([a-zA-Z_]\w*)[\t ]*.*?(?:,[\t ]*([a-zA-Z_]\w*).*?)*)\)"
    )

    vars_dict = {}
    offset = 0

    while True:
        chunk = code[offset:]

        if bool(def_regex.match(chunk)):
            print("Matched function pattern. Feature not implemented, yet.")

        elif bool(variable_regex.match(chunk)):
            first_match = variable_regex.search(chunk)
            second_match = variable_regex.search(chunk[first_match.span()[1] :])

            if not bool(second_match):
                while True:
                    variable_name = "".join(random.choices(charset, k=8))
                    if variable_name in vars_dict:
                        continue
                    break

                vars_dict[first_match.group(1)] = variable_name

                code = code[: offset - 1] + re.sub(
                    r"\b{}\b".format(first_match.group(1)), chunk, variable_name
                )

            else:
                while True:
                    variable_name = "".join(random.choices(charset, k=8))
                    if variable_name in vars_dict:
                        continue
                    break

                code = (
                    code[: offset - 1]
                    + re.sub(
                        r"\b{}\b".format(first_match.group(1)),
                        chunk[: second_match.span()[1] - 1],
                        variable_name,
                    )
                    + chunk[second_match.span()[0] :]
                )

        else:
            break

    return code
