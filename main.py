import logging
import sys
from functools import reduce
from operator import or_

import click

from helper import validate_inputs, parse_dict_file, read_input, slice_str, check_scrambled_form

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()


def scrmabled_strings(dictionary, input, debug=False):
    """do the scrmabled strings search"""
    try:
        validate_inputs(dictionary, input)
    except Exception as ex:
        print(ex)
        return
    dict_words = parse_dict_file('dict.txt')
    dict_total = sum([len(x) for x in dict_words.values()])
    input_line = read_input('input.txt')
    found_words = set()

    # print the searching words
    print(f'Search: {reduce(or_, dict_words.values())}')

    # create cursor for each length of dict word, all start from 0
    cursor = dict.fromkeys(dict_words.keys(), 0)

    while cursor:
        for word_len in dict_words.keys():
            if word_len not in cursor:
                # this length of word already finished
                continue
            slice = slice_str(input_line, cursor[word_len], word_len)

            if not slice:
                #  is search ended, pop this len from cursor
                cursor.pop(word_len)
                continue
            for word in dict_words[word_len].copy():
                if check_scrambled_form(word, slice):
                    # found, pop it from target dict
                    logger.debug(f'Pop "{word}" matching with "{slice}"')
                    dict_words[word_len].remove(word)
                    found_words.add(word)
            cursor[word_len] += 1
    dict_rest = sum([len(x) for x in dict_words.values()])

    # print the searching result
    logger.info(f'Word matched: {found_words}')

    logger.info(f'Word not matched: {reduce(or_, dict_words.values())}')

    return dict_total - dict_rest


@click.command()
@click.option('--dictionary', help='path to dictionary file')
@click.option('--input', default='', help='path to input file')
@click.option('--debug', default=False, help='print loop step info for debugging')
def main(dictionary, input, debug):
    """just a wrapper entry"""
    if debug:
        logger.setLevel(logging.DEBUG)
    scrmabled_strings(dictionary, input, debug)


if __name__ == "__main__":
    main()
    sys.exit(0)
