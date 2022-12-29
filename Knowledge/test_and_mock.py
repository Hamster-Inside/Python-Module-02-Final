from requests import get


def check_first_line_more_than(x):
    url = 'https://api.pwnedpasswords.com/range/a94a8'
    response = get(url)
    counter = response.text.splitlines()[0].split(':')[1]
    if int(counter) > x:
        return True
    else:
        return False


check_first_line_more_than(10)
