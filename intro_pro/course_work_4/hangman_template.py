# Coding Challenge 3, hangman.py
# Name:
# Student No:

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):

    return random.choice(all_words)


# end of helper code
# -----------------------------------

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


def is_word_guessed(word, letters_guessed):
    letters_guessed = [x for x in letters_guessed]
    word = [z for z in word]
    maybe = all(x in letters_guessed for x in word)
    # looping over list word and checking if that item is in list letters_guessed
    # all() will only return true if all the items are else false
    return maybe

def get_guessed_word(word, letters_guessed):
    placeholder = ''
    for x in word:
        if x in letters_guessed:
            placeholder += x
        elif x not in letters_guessed:
            placeholder += '_ '
    return placeholder

def get_remaining_letters(letters_guessed):
    alphabet = string.ascii_lowercase
    alphabet = [x for x in alphabet]
    for x in letters_guessed:
        if x in alphabet:
            alphabet.remove(x)
    alphabet = ''.join(alphabet)
    return alphabet


def hangman(word):
    print("Welcome to Hangman Ultimate Edition")
    print(f"I am thinking of a word that is {len(word)} letters long")
    print("-" * 12)

# ---------- Challenge Functions (Optional) ----------

def get_score(name):
    pass

def save_score(name, score):
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

def main():
    # Uncomment the line below once you have finished testing.
    # word = choose_random_word(wordlist)

    # Uncomment the line below once you have implemented the hangman function.
    # hangman(word)
    GUESSES = 6

    word = load_words()
    word = random.choice(word)

    hangman(word)
    print(f'You have {GUESSES} guesses left.')
    available_letters = string.ascii_lowercase
    print(f'Available letters: {available_letters}')
    guessed_letter = input('Please guess a letter: ').lower()
    
    get_guessed_word(word, guessed_letter)

# Driver function for the program
if __name__ == "__main__":
    main()
