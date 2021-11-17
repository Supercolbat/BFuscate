import argparse

def main():
    parser = argparse.ArgumentParser(description="Process CLI args")
    parser.add_argument(
        "-i", "--input", help="File to obfuscate", required=True, type=str
    )
    parser.add_argument(
        "-r",
        "--replace",
        help="Replace the file specified",
        required=False,
        default=False,
        type=bool,
    )
    parser.add_argument(
        "-ol",
        "--one-liner",
        help="Add the one liner technique",
        required=False,
        default=False,
        type=bool,
    )
    args = parser.parse_args()

    convert_file(args)