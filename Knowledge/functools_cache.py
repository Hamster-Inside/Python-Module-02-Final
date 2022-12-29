from functools import cache

@cache
def tell_me_something(word):
    print(f'Przetwarzam slowo{word}')
    vowels = [letter for letter in word if letter in 'aeiouy']

    return {
        'len': len(word),
        'vowels':len(vowels)
    }

print(tell_me_something('asdfasdfasdlfkj'))
tell_me_something.cache_clear()
print(tell_me_something('kokos'))
print(tell_me_something('asdfasdfasdlfkj'))
