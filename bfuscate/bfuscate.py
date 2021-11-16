"""
A simple python obfuscator.
usage: python bfuscate.py -h
"""

import os
import sys
import argparse
import time

import methods

try:
    import python_minifier
except ModuleNotFoundError as e:
    os.system("python -m pip install python_minifier")
    print("[✔] Successfully installed required modules. Try running BFuscate again.")
    sys.exit()


# Parse arguments
parser = argparse.ArgumentParser()
g_other = parser.add_argument_group("other")
g_configuration = parser.add_argument_group("configuration")
g_flags = parser.add_argument_group("flags")
g_output = parser.add_argument_group("output")


g_configuration.add_argument(
    "-m", "--method",
    choices=["len", "lambda"], default="lambda",
    help="method of obfuscation"
)
g_configuration.add_argument(
    "--defend",
    action="store_true",
    help="self-defends the code (WIP)"
)
g_configuration.add_argument(
    "--rename-vars",
    choices=["I", "O", "hex", "random"],
    help="obfuscates variable names (WIP)"
)

g_flags.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="outputs verbose information (WIP)"
)

parser.add_argument(
    "file",
    type=str,
    help="target file for obfuscation"
)
g_output.add_argument(
    "-o", "--output",
    type=str,
    help="output destination"
)

args = parser.parse_args()

if __name__ == "__main__":
    filename = args.file
    output = args.output if args.output else filename.split(".")[0] + "_BFUSCATED.py"

    start = time.time()

    with open(filename) as f:
        code = f.read().replace("\"", "'")
        minified = python_minifier.minify(code)

    if args.method == "lambda":
        RESULT = methods.lambda_bfuscate(minified, args)
    elif args.method == "len":
        RESULT = methods.len_bfuscate(minified, args)
    else:
        print(f"[×] Unknown obfuscation method '{args.method}'")
        sys.exit()

    with open(output, "w+") as f:
        f.write(RESULT)

    print(f"[✔] Successfully obfuscated: {filename}")
    print(f"Before\t\t{len(code)} characters")
    print(f"Minified\t{len(minified)} characters")
    print(f"Obfuscated\t{len(RESULT)} characters")
    print(f"\nTime elapsed: {int((time.time() - start) * 1000)} milliseconds")
