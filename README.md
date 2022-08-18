<h1 align="center">sus</h1>
<h3 align="center">A purely <ins>sussy</ins> obfuscator for Python</h3>

<br>

<p align="center">
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
  <img src="https://img.shields.io/badge/is%20it%20good%20yet%3F-no-651cdb.svg" alt="is it good yet? no">
</p>

## :rotating_light: Sus

If you are looking for an obfuscator to protect your Python source, then this project will not be useful for you... yet!

For now, I suggest you to take a look at [pyarmor](https://github.com/dashingsoft/pyarmor) or [cython](https://github.com/cython/cython).

For the record, as of right now, the whole source can be recovered by simply replacing the very first word in the output (`exec`) with a `print`.

My goal is to have this *not* be the case, but at least it looks mildly intimidating at first glace.

## :rocket: Sus

### Sus

- Python 3.8+
  - Note: I have not checked if this works in any other Python version 
- A computer, at least one hand (or alternatives), electricity, a consciousness, etc...

```sh
git clone --depth=1 https://github.com/Supercolbat/BFuscate.git
cd BFuscate
python3 setup.py install
python3 -m bfuscate -h
```

## :crystal_ball: Sus
See `obfuscate_me_BFUSCATED.py` to get a feel for BFuscate.

It's constantly updated because its the file I use for testing.

## :wrench: Sus
```
usage: __main__.py [-h] [-o OUTPUT] file

positional arguments:
  file                  target file for obfuscation

optional arguments:
  -h, --help            show this help message and exit

output:
  -o OUTPUT, --output OUTPUT
                        output destination
```

As a result of calling the program as a module, the file name *will* be `__main__.py`.


### Sussing a file
```sh
python3 -m bfuscate obfuscate_me.py

python3 obfuscate_me_BFUSCATED.py
```

### Sussing *to* a file
The positional arguments are not positional, meaning that the output flag can come before or after the file.
```sh
python3 -m bfuscate --output another_foo.py obfuscate_me.py
# or
python3 -m bfuscate obfuscate_me.py -o foo.py

python3 foo.py
python3 another_foo.py
```
