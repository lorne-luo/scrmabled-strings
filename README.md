# scrmabled-strings

This project could find scrmabled-form word from input file. 


## Requirements

This project require Python version 3.6 or above due to used [f-string formatting](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) which is a new feature since Python 3.6.
- Python 3.6 or above
- Git


## Installation
Git clone this repo, create virtualenv and run pip install

The only one third-party package needed is [Click](https://click.palletsprojects.com/en/7.x/) which is used to handle command line inputs.
```
git clone https://github.com/lorne-luo/scrmabled-strings.git 
cd scrmabled-strings
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## How to run
Check command line usage with `--help`
```
>>> python main.py --help

Usage: main.py [OPTIONS]

  Find scrmabled-form word from input file

Options:
  -d, --dictionary TEXT  path to dictionary file  [required]
  -i, --input TEXT       path to input file  [required]
  --debug                print verbose info for debugging
  --help                 Show this message and exit.

```

Run with demo:
```
>>> python main.py --dictionary dict.txt --input input.txt --debug

DEBUG:root:Search: {'dnrbt', 'apxaj', 'abd', 'pjxdn', 'axpaj'}
DEBUG:root:Pop "apxaj" as match with "aapxj"
DEBUG:root:Pop "axpaj" as match with "aapxj"
DEBUG:root:Pop "pjxdn" as match with "pxjdn"
DEBUG:root:Pop "dnrbt" as match with "dnrbt"
DEBUG:root:Words found: {'pjxdn', 'dnrbt', 'axpaj', 'apxaj'}
DEBUG:root:Words not found: {'abd'}

4 words from the dictionary are found in the input.
```

## How to do programming integration
Copy source code into you project, call with snippet below:
```
from main import scrmabled_strings

found_counter = scrmabled_strings('dict.txt','input.txt')
```
## Implementation
1. **Scrmabled word identification**

It used a 26 length bytes-map to identify scrmabled form word, each value represent the frequency for alphabet a-z.

The limitation of this design is due to each byte only support int up to 255, it will raise error if one dict word have more than 255 char 'a' in it. 
```
from helper import get_byte_map
map = get_byte_map('abbz')
print(map)
```
```
bytearray(b'\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
```

```
# let's check int value
print([x for x in map])
```
```
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```


2. **Acceleration by dict word length group**

All dict words are group by its length, so each slice from input file could be reuse for same length dict word
```
from pprint import pprint
from helper import get_dict_maps
word_map_groups = get_dict_maps({'axpaj', 'apxaj', 'pjxdn', 'dnrbt', 'abd'})
pprint(word_map_groups)
```
```
{3: {'abd': bytearray(b'\x01\x01\x00\x01\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')},
 5: {'apxaj': bytearray(b'\x02\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x01\x00\x00\x00\x00\x00\x01'
                        b'\x00\x00\x00\x00\x00\x00\x00\x01'
                        b'\x00\x00'),
     'axpaj': bytearray(b'\x02\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x01\x00\x00\x00\x00\x00\x01'
                        b'\x00\x00\x00\x00\x00\x00\x00\x01'
                        b'\x00\x00'),
     'dnrbt': bytearray(b'\x00\x01\x00\x01\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x01\x00\x00'
                        b'\x00\x01\x00\x01\x00\x00\x00\x00'
                        b'\x00\x00'),
     'pjxdn': bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'
                        b'\x00\x01\x00\x00\x00\x01\x00\x01'
                        b'\x00\x00\x00\x00\x00\x00\x00\x01'
                        b'\x00\x00')}
}
```
 
## How to test
Simply run
```
python3 -m unittest discover
```

## TBD
- Currently only do the search for the first line of input file, will solve it later
- Will create Dockerfile later 
