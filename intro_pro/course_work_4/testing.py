import random
import string
import csv


def load_words():
    print('Loading word list from file: words.txt')
    try:
        with open('word.txt', 'r') as file:
            words = file.readlines()
    except FileNotFoundError as error:
        print(f'Sorry, {error}')
    except Exception as error:
        print(error)
    else:
        words = ' '.join(words)
        words_list = words.split()
        print(f'{len(words_list)} words loaded.')
        return words_list    
one = load_words()
secret_word = random.choice(one)
print(secret_word)

letters_guessed = ['m', 'a', 'n', 's', 'x', 'l', 'o', 'u', 'd']
word = 'mans'

def is_word_guessed(word, letters_guessed):
    letters_guessed = [x for x in letters_guessed]
    word = [z for z in word]
    maybe = all(x in letters_guessed for x in word)
    # looping over list word and checking if that item is in list letters_guessed
    # all() will only return true if all the items are else false
    return maybe


one = is_word_guessed(word, letters_guessed)
# print(one)

letters_guessed = ['m', 'a', 'n', 's', 'x', 'l', 'o', 'u', 'd']
word = 'mansqwoud'
def get_guessed_word(word, letters_guessed):
    placeholder = ''
    for x in word:
        if x in letters_guessed:
            placeholder += x
        elif x not in letters_guessed:
            placeholder += '_ '
    return placeholder

# one = get_guessed_word(word, letters_guessed)
# print(one)

def get_remaining_letters(letters_guessed):
    alphabet = string.ascii_lowercase
    alphabet = [x for x in alphabet]
    for x in letters_guessed:
        if x in alphabet:
            alphabet.remove(x)
    alphabet = ''.join(alphabet)
    return alphabet

# one = get_remaining_letters(letters_guessed)
# print(one)

name = 'mansoud'
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
w = csv.writer(open('output.csv', 'w'))
for key, val in dict.items():
    w.writerow([key, val])

def get_score(name):
    with open('score_table.csv', 'w') as file:
        file = file.readline()
        print(file)
        print(type(file))
        # if name not in file:
        #     print('Sorry, name not found!')
        # else:
        #     high_score = file.get(name)
        #     return high_score

# one = get_score(name)
# print(one)


def save_score(name, score):
    pass
# one = save_score(name, 12334)
# print(one)


def main():
    load_words()

    