import random
import string # all letters and all numbers


# 1. create a dictionay named password_lookup that contains usernames as keys and passwords as associated string values. make up data for five entries.

password_lookup = {'one':'onehundred', 'two':'twohundred', 'three':'threehund', 'four':'fourhundred', 'five':'fivehundred'}

# print(password_lookup.keys())
# print(password_lookup.values())
# print(password_lookup.items())

# 2. write a program that creates an initially empty dictionay named password_lookup, prompting one by one for usernames and passwords (until a username of 'z' is read) entering each into the dictionary.

def user():
    password_lookup = {}
    username = ''
    password = ''

    while True:
        username = input('please enter username: ')
        if username == 'z':
            break
        elif username in password_lookup:
            print('username already exist, try another one!')
            username = input('please enter username: ') 
        password = input('please enter password: ')

        password_lookup.update({username:password})
    print(password_lookup)

# user()

# 3. create a dictionary named password_hint that contains email addresses as keys, and associated values that contain both the users 'password security question' and the anser to the question. make up data for dictionary entries.

def pass_hint():
    password_hint = {}
    email = ''
    question = ['what city you born?', 'what is your moms name']
    answer = ''

    while True:
        email = input('Please enter email: ')
        if email == 'quit':
            break
        elif '@' not in email:
            print('invalid emial!!')
            email = input('Please enter email: ')
        elif email in password_hint:
            print('email already exist, try again!')
            email = input('Please enter email: ')
        
        quest = random.choice(question)
        print(quest)
        answer = input('your answer: ')

        password_hint.update({email:[quest, answer]})

    print(password_hint)

# pass_hint()


# 4. create a dictionary named member_table that contains users' email addresses as keys, and answers to their password hints as the associated values, and a function that generates a temporary new password and stored in the table.

def generate_word():
    letters = string.ascii_lowercase
    letters_b = string.ascii_uppercase
    numbers = string.digits
    # making a list of letters and numbers
    one = [x for x in letters]
    two = [x for x in letters_b]
    three = [x for x in numbers]
    # making a list of letters and numbers
    all = one + two + three
    new_pass = ''
    for x in range(0, random.randint(1, len(all)) + 1):
        new_pass += random.choice(all)
    return new_pass


def member():
    member_table = {}
    email = ''
    pass_hint = ''
    new_password = generate_word()

    while True:
        email = input('Enter your email: ')
        if email == 'quit':
            break
        elif email in member_table:
            print('email exist, try again!')
            email = input('Enter your email: ')
        elif '@' not in email:
            print('not valid! Try again!!')
        pass_hint = input('Enter password hint: ')
        member_table.update({email:[pass_hint, new_password]})
    return member_table

# one = member()
# print(one)

# 5. declare a set named vowels containing the strings 'a', 'e', 'i', 'o', 'u'. create a function called count_vowels that promt the user for any english word and displays how many vowel if contains.


def count_vowels():
    word = input('Please enter a word: ')
    vowels = {'a', 'e', 'i', 'o', 'u'}
    num_of_vowels = 0
    for x in word:
        if x in vowels:
            num_of_vowels += 1
    return num_of_vowels

# one = count_vowels()
# print(one)



# 6. create a function called word_intersection that prompts the user for two english words, and displays which letters the two words have in common. convert each string to a set type in order to sloce this problem. 

def word_intersection():
    first_word = input('please enter your first word: ')
    second_word = input('please enter your second word: ')

    first_word = {x for x in first_word}
    second_word = {x for x in second_word}

    in_both = first_word.intersection(second_word)
    return in_both

# one = word_intersection()
# print(one)

# 7. create a function called word_difference that prompts the user for two english words, and displays which letter are in the first word but not the second. convert each string to a set type in order to solce this.

def word_difference():
    first_word = input('please enter your first word: ')
    second_word = input('please enter your second word: ')

    first_word = {x for x in first_word}
    second_word = {x for x in second_word}

    defference = first_word.difference(second_word)
    return f'letters in first and not in second word: {[x for x in defference]}'

# one = word_difference()
# print(one)


# 8. create a function called get_missing_letters that prompts the user for two English words and displays which letter of the alphabet are in neither of the two words. convert each string to a set type in orver to solve this.

def get_missing_letters():
    alphabet = {x for x in string.ascii_lowercase}

    first_word = input('please enter your first word: ')
    second_word = input('please enter your second word: ')

    first_word = {x.lower() for x in first_word}
    second_word = {x.lower() for x in second_word}
    in_neither = alphabet.difference(first_word, second_word)
    return in_neither

# one = get_missing_letters()
# print(one)

# 9. create a function called word_difference that prompts the user for two english words, and displays which letters are in either the first word or the seccond word, but not both words. convert each string to a set type in order to solce this. 

def word_sdifference():
    first_word = input('please enter your first word: ')
    second_word = input('please enter your second word: ')

    first_word = {x.lower() for x in first_word}
    second_word = {x.lower() for x in second_word}

    one = first_word.symmetric_difference(second_word)
    return one

# one = word_sdifference()
# print(one)

