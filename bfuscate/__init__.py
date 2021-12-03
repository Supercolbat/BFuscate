"""
BFuscate: an efficient obfuscator for Python code.

"""

__app_name__ = "BFuscate"
__author__   = "Joey Lent (Supercolbat)"
__version__  = "0.1.0"
__license__  = "MIT"

try:
    import python_minifier
except ModuleNotFoundError as e:
    import os
    import sys

    os.system("python -m pip install python_minifier")
    print("[✔] Successfully installed required modules. Try running BFuscate again.")
    sys.exit(1)