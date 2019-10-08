import logging
import sys

import click

from helper import validate_inputs, parse_dict_file, read_input, slice_str, check_scrambled_form, get_dict_maps, \
    get_byte_map

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


def scrmabled_strings(dictionary, input):
    """do the scrmabled strings search"""
    validate_inputs(dictionary, input)

    dict_words = parse_dict_file('dict.txt')
    length_grouped_word_maps = get_dict_maps(dict_words)
    dict_total = len(dict_words)
    input_line = read_input('input.txt')
    found_words = set()

    # print the searching words
    logger.debug(f'Search: {dict_words}')

    # create cursor for each length channel of dict word, all start from 0
    dict_cursor = dict.fromkeys(length_grouped_word_maps.keys(), 0)

    while dict_cursor:
        for word_len in length_grouped_word_maps.keys():
            if word_len not in dict_cursor:
                # this length of word already finished
                continue

            slice = slice_str(input_line, dict_cursor[word_len], word_len)
            if not slice:
                #  is search ended, pop this len from cursor
                dict_cursor.pop(word_len)
                continue

            slice_byte_map = get_byte_map(slice)

            for word in list(length_grouped_word_maps[word_len].keys()):
                word_map = length_grouped_word_maps[word_len][word]
                if check_scrambled_form(word, word_map, slice, slice_byte_map):
                    # found, pop it from target dict
                    logger.debug(f'Pop "{word}" as match with "{slice}"')
                    length_grouped_word_maps[word_len].pop(word)
                    found_words.add(word)
            dict_cursor[word_len] += 1
    dict_rest = sum([len(x) for x in length_grouped_word_maps.values()])

    # print the searching result
    logger.debug(f'Words found: {found_words}')

    logger.debug(f'Words not found: {dict_words-found_words}')

    return dict_total - dict_rest


@click.command()
@click.option('--dictionary', '-d', required=True, help='path to dictionary file')
@click.option('--input', '-i', required=True, help='path to input file')
@click.option('--debug', is_flag=True, default=False, help='print loop step info for debugging')
def main(dictionary, input, debug):
    """Find scrmabled-form word from input file """
    if debug:
        logger.setLevel(logging.DEBUG)
    try:
        result = scrmabled_strings(dictionary, input)
        print(f'{result} words from the dictionary are found in the input.')
    except Exception as ex:
        print(ex)
        return


if __name__ == "__main__":
    main()
    sys.exit(0)
