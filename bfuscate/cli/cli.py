import time
import python_minifier

from .arguments import parse_args

def main():
    # temporary
    args = parse_args()

    filename = args.file
    output = args.output if args.output else filename.split(".")[0] + "_BFUSCATED.py"

    start = time.perf_counter()

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
    print(f"\nTime elapsed: {(time.perf_counter() - start)} seconds")