import logging
logging.basicConfig(level=logging.DEBUG)
# --------------------------------------------------------------------------------------
# with open('plik.txt') as input_file, open('wynik.txt') as output_file:
#     for line in input_file

# --------------------------------------------------------------------------------------
def power(x):
    logging.debug(f'power run with {x}')
    try:
        return x ** 2
    except TypeError:
        logging.warning('run with not num variable')
        try:
            return int(x) ** 2
        except ValueError:
            logging.critical('its not a num')


score = power('asdf')
print(score)
logging.info(f'score = {score}')

# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL
# --------------------------------------------------------------------------------------
from requests import get

word = input('Jakiego rymu będziemy szukali? ')
url = 'http://api.datamuse.com/words?rel_rhy=' + word

with get(url) as content:
    for row in content.json():
        print(row['word'])
# --------------------------------------------------------------------------------------
