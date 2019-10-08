import os
import sys

import click


def validate_inputs(dictionary, _input):
    """validate input file existed"""

    if not os.path.isfile(dictionary):
        raise Exception(f'Can\'t find {dictionary}, please input a valid relative filename or absolute path.')

    if not os.path.isfile(_input):
        raise Exception(f'Can\'t find {_input}, please input a valid relative filename or absolute path.')


def check_scrambled_form(source, target):
    """return True if source is a scrambled_form(include equal) of target"""
    if not isinstance(str, source) or not isinstance(str, target):
        raise Exception('check_scrambled_form() only accept str as param.')

    raise NotImplementedError


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
