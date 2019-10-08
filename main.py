import os
import sys
from collections import defaultdict

import click


def validate_inputs(dictionary, _input):
    """validate input file existed"""

    if not os.path.isfile(dictionary):
        raise Exception(f'Can\'t find {dictionary}, please input a valid relative filename or absolute path.')

    if not os.path.isfile(_input):
        raise Exception(f'Can\'t find {_input}, please input a valid relative filename or absolute path.')


def parse_dict_file(dic_file):
    """get dict words and group them by length"""
    dict_words = defaultdict(list)

    with open(dic_file) as file_handler:
        for line in read_line(file_handler):
            word = line.strip()
            dict_words[len(word)].append(word)
    return dict_words


def read_line(file):
    """Generator to read a large file lazily"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def check_scrambled_form(source, target):
    """return True if source is a scrambled_form(include equal) of target"""
    if not isinstance(source, str) or not isinstance(target, str):
        raise TypeError('check_scrambled_form() only accept str as param.')

    if not len(source) or not len(target):
        raise Exception('Please pass valid str into check_scrambled_form().')

    if source == target:
        # shortcut for equal
        return True
    if source[0] == target[0] and source[-1] == target[-1] and set(source) == set(target):
        return True
    return False


def slice_str(src, start, length):
    """slice str by start and len"""
    if start < 0:
        raise ValueError('start should be not less than 0.')
    if length < 1:
        raise ValueError('length should be greater than 0.')
    end = start + length
    if end > len(src):
        return None

    return src[start:end]


@click.command()
@click.option('--dictionary', help='path to dictionary file')
@click.option('--input', default='', help='path to input file')
def main(dictionary, input):
    try:
        validate_inputs(dictionary, input)
    except Exception as ex:
        print(ex)
        return


if __name__ == "__main__":
    main()
    sys.exit(0)
