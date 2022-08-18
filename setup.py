from setuptools import setup
from typing import List
import bfuscate


def long_description() -> str:
    with open("README.md", encoding="utf-8") as file:
        return file.read()


def install_requires() -> List[str]:
    with open("requirements.txt", encoding="utf-8") as file:
        return file.read().strip().splitlines()


setup(
    name="BFuscate",
    version=bfuscate.__version__,
    description=bfuscate.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author=bfuscate.__author__,
    author_email="supercolbat@protonmail.com",
    license=bfuscate.__license__,
    keywords=["obfuscator"],
    python_requires=">=3.6",
    download_url="https://github.com/Supercolbat/BFuscate/",
    install_requires=install_requires(),
    entry_points={"console_scripts": ["bfuscate = bfuscate.__main__:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    project_urls={"GitHub": "https://github.com/Supercolbat/BFusacte"},
)
