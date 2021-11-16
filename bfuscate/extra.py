import re
import random

# \([\t ]*(?:([a-zA-Z_][\w\d]*)(?:,[\t ]*([a-zA-Z_][\w\d]*)[\t ]*(?::[\t ]*\w+|=[\t ]\d)?)*)\)

def rename_variables(charset, code) -> str:
    variable_regex = r"\b([a-zA-Z_]\w*)\s*:?=(?!=)[\t ]*."
    def_regex = r"[\t ]*def ([a-zA-Z_]\w*)\((?:([a-zA-Z_]\w*)[\t ]*.*?(?:,[\t ]*([a-zA-Z_]\w*).*?)*)\)"

    vars_dict = {}
    offset = 0

    # for segment in [l.split(";") for l in code.split("\n")]:
    while True:
        chunk = code[offset:]

        if bool(re.match(def_regex, chunk)):
            print("Matched function pattern. Feature not implemented, yet.")

        elif bool(re.match(variable_regex, chunk)):
            first_match = re.search(variable_regex, chunk)
            second_match = re.search(variable_regex, chunk[first_match.span()[1]:])
            
            if not bool(second_match):
                while True:
                    variable_name = "".join(random.choices(charset, k=8))
                    if variable_name in vars_dict: continue
                    break
                
                vars_dict[first_match.group(1)] = variable_name

                code = code[:offset - 1]
                     + re.sub(r"\b{}\b".format(first_match.group(1)), chunk, variable_name)
            
            else:
                while True:
                    variable_name = "".join(random.choices(charset, k=8))
                    if variable_name in vars_dict: continue
                    break
                    
                code = code[:offset - 1] \
                     + re.sub(r"\b{}\b".format(first_match.group(1)), chunk[:second_match.span()[1]-1], variable_name) \
                     + chunk[second_match.span()[0]:]
        
        else:
            break
    
    return code
