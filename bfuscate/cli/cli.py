import time
import python_minifier

from bfuscate.obfuscate import obfuscate
from .arguments import parse_args


def main():
    # temporary
    args = parse_args()

    filename = args.file
    output = args.output if args.output else filename.split(".")[0] + "_BFUSCATED.py"

    start = time.perf_counter()

    with open(filename) as f:
        code = f.read().replace('"', "'")
        minified = python_minifier.minify(code)

    result = obfuscate(minified)

    with open(output, "w+") as f:
        f.write(result)

    print(f"[✔] Successfully obfuscated: {filename}")
    print(f"Before\t\t{len(code)} characters")
    print(f"Minified\t{len(minified)} characters")
    print(f"Obfuscated\t{len(result)} characters")
    print(f"\nTime elapsed: {(time.perf_counter() - start)} seconds")
