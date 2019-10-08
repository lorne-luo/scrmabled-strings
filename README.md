# scrmabled-strings

This project could find scrmabled-form word from input file. 


## Requirements

This project require Python version 3.6 or above due to used [f-string formatting](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) which is a new feature since Python 3.6.
- Python 3.6 or above
- Git


## Installation
Git clone this repo, create virtualenv and run pip install

The only one third-party package needed is [Click](https://click.palletsprojects.com/en/7.x/) which is used to handle command line interfaces.
```
git clone https://github.com/lorne-luo/scrmabled-strings.git 
cd scrmabled-strings
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## How to run
Run with demo:
```
>>> python main.py --dictionary dict.txt --input input.txt --debug

DEBUG:root:Search: {'dnrbt', 'apxaj', 'abd', 'pjxdn', 'axpaj'}
DEBUG:root:Pop "apxaj" matching with "aapxj"
DEBUG:root:Pop "axpaj" matching with "aapxj"
DEBUG:root:Pop "pjxdn" matching with "pxjdn"
DEBUG:root:Pop "dnrbt" matching with "dnrbt"
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

 
## How to test
Simply run
```
python3 -m unittest discover
```
