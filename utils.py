from functools import reduce
import math


def encrypt(code) -> str:
    split_code = code.split("#")
    output = ""

    split_code.append(str(code.__hash__()))

    for a, b in zip(split_code[1], split_code[2] * math.ceil(len(split_code[1]) / len(split_code[2]))):
        output += hex(ord(a) ^ ord(b))[2:].rjust(2, "0")

    return split_code[0] + "#" + output + "#" + split_code[2]


def find(substring, string) -> list:
    indexes = []
    index = -1

    while (ind := string[index + 1:].find(substring)) != -1 and index < len(string):
        index = ind + index + 1
        indexes.append(index)

    return indexes


def split(num) -> tuple:
    nums = [num]
    ptr = 0
    offset = 0
    last_num = 0

    while ptr < len(nums):
        while not nums[ptr] in [1, 2, 3, 5, 7]:
            if nums[ptr] == last_num:
                if nums[ptr + 1:]:
                    offset += reduce(lambda x, y: x * y, nums[ptr + 1:])
                else:
                    break

                nums[ptr] += 1

            last_num = nums[ptr]

            for i in [2, 3, 5, 7]:
                if nums[ptr] % i == 0:
                    nums[ptr] //= i
                    nums.append(i)
                    break

        ptr += 1

    nums = sorted(nums)
    l = {}
    for i in nums:
        if i not in l and nums.count(i):
            l[i] = nums.count(i)

    return l, offset


# Credits to https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html
from math import ceil, log


def encode(num, depth) -> str:
    if num == 0:
        return "(lambda:_).__code__.co_argcount"
    if num <= 8:
        return "(lambda {}:_).__code__.co_argcount".format(
            ",".join(["_" * i for i in range(1, num + 1)])
        )
    return "({})".format(convert(num, depth + 1))


def convert(num, depth=0) -> str:
    if num == 0:
        return "(lambda:_).__code__.co_argcount"

    RESULT = ""
    while num:
        base = shift = 0
        diff = num
        span = int(ceil(log(abs(num), 1.5))) + (16 >> depth)
        for test_base in range(span):
            for test_shift in range(span):
                test_diff = abs(num) - (test_base << test_shift)
                if abs(test_diff) < abs(diff):
                    diff = test_diff
                    base = test_base
                    shift = test_shift
        if RESULT:
            RESULT += "+" if num > 0 else "-"
        elif num < 0:
            base = -base
        if shift == 0:
            RESULT += encode(base, depth)
        else:
            RESULT += "({}<<{})".format(
                encode(base, depth),
                encode(shift, depth)
            )
        num = diff if num > 0 else -diff
    return RESULT
