import argparse


def parse_args():
    # Parse arguments
    parser = argparse.ArgumentParser()
    g_other = parser.add_argument_group("other")
    g_configuration = parser.add_argument_group("configuration")
    g_flags = parser.add_argument_group("flags")
    g_output = parser.add_argument_group("output")

    """
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
    """

    parser.add_argument("file", type=str, help="target file for obfuscation")
    g_output.add_argument("-o", "--output", type=str, help="output destination")

    args = parser.parse_args()

    return args
