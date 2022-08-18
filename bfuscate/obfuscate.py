import random
from bfuscate.methods import lambda_bfuscate, len_bfuscate
from bfuscate.constants import HEADER


def obfuscate(source: str) -> str:
    """
    Combines available obfuscation methods to
    generate the source.
    """

    methods = (lambda_bfuscate, len_bfuscate)

    return HEADER + "+".join(random.choice(methods)(char) for char in source)
