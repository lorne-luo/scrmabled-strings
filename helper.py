import os
from collections import defaultdict


def validate_inputs(dictionary, _input):
    """validate input file existed"""

    if not os.path.isfile(dictionary):
        raise Exception(
            f"Can't find {dictionary}, please input a valid relative filename or absolute path."
        )

    if not os.path.isfile(_input):
        raise Exception(
            f"Can't find {_input}, please input a valid relative filename or absolute path."
        )


def parse_dict_file(dict_file):
    """get dict words and group them by length"""
    dict_words = set()

    with open(dict_file) as file_handler:
        for line in read_line(file_handler):
            word = line.strip()
            dict_words.add(word)
    return dict_words


def get_dict_maps(words):
    """get a dict group by word length"""
    dict_maps = defaultdict(dict)

    for line in words:
        word = line.strip()
        dict_maps[len(word)][word] = get_byte_map(word)

    return dict_maps


def read_input(input_file):
    """get first line as input, ignore below"""
    lines = []

    with open(input_file) as file_handler:
        for line in read_line(file_handler):
            lines.append(line.strip())
    return lines


def read_line(file):
    """Generator to read a large file lazily"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def check_scrambled_form(source, source_map, target, target_map):
    """return True if source is a scrambled_form(include equal) of target"""
    if not isinstance(source, str) or not isinstance(target, str):
        raise TypeError("check_scrambled_form() only accept str as param.")

    if not len(source) or not len(target):
        raise Exception("Please pass valid str into check_scrambled_form().")

    if source == target:
        # shortcut for equal
        return True
    if source[0] == target[0] and source[-1] == target[-1] and source_map == target_map:
        return True
    return False


def get_byte_map(word):
    """Bytes map to store char frequency for word, reach byte can store int up to 255"""
    arr = bytearray(26)
    for c in word:
        if ord(c) < ord("a") or ord(c) > ord("z"):
            # skip invalid char
            continue
        index = ord(c) % ord("a")
        if arr[index] == 255:
            raise ValueError(
                f"Char `{c}` in word `{word}` exceed 255, which is a invalid input for this system."
            )
        arr[index] += 1
    return arr


def slice_str(src, start, length):
    """slice str by start and len"""
    if start < 0:
        raise ValueError("start should be not less than 0.")
    if length < 1:
        raise ValueError("length should be greater than 0.")
    end = start + length
    if end > len(src):
        return None

    return src[start:end]
