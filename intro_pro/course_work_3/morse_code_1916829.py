# Coding Challenge 2
# Name: Mansoud Mansouri
# Student No: 1916829

# A Morse code encoder/decoder

morse_dic = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '.':'.-.-.-', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', '?':'..--..', '!':'-.-.--'}



def print_intro():
    '''Displays welcome note and the porpuse of this program.'''
    print('''Welcome to Wolmorse
This program encode and decode Morse code.''')


def get_input():
    '''
    Requiring a message and mode from the user.

            Parameter:
                None

            Returns:
                message (str): user's message
                mode (str): user's chosen mode
    '''
    mode = input('Would you like to encode (e) or decode (d): ')
    mode = mode.lower()
    #continuesly looiing over for the user to enter the correct mode
    while mode not in ['e', 'd']:
        print('Invalid mode.')
        mode = input('Would you like to encode (e) or decode (d): ')
    if mode == 'e':
        message = input('What message would you like to encode? ')
        message = message.upper()
        return mode, message
    elif mode == 'd':
        message = input('What message would you like to decode? ')
        message = message.upper()
        return  mode, message


def encode(message):
    '''
    Takes in a message, returns morse code of the message.

            Parameter:
                message (str): string of message

            Returns:
                message's morse code (str)
    '''
    cipher =''
    # iterate over the message and if its not a free space
    # search dictionary for carresponding morse code
    # if its 1 space add 3 spaces
    # return the result
    for letter in message:
        if letter != ' ':
            cipher += morse_dic[letter] + ' '
        else:
            cipher += '   '
    return cipher


def decode(message):
    '''
    Takes morse code and returns the English equivelent.

            Parameter:
                message (morse code)

            Returns:
                decipher: message deciphered
    '''
    decipher = ''
    # splitting the message into it's indivitual words
    # splitting each word into it's indivitual letters 
    # iterate over the dictonary to find the carresponding letter
    words = message.split('   ')
    for morse_word in words:
        chars = morse_word.split()
        for char in chars:
            for key, value in morse_dic.items():
                if char == value:
                    decipher += key
        decipher += ' '
    return decipher


def main():
    print_intro()
    mode, message = get_input()
    if mode == 'e':
        message = encode(message)
        print(message)
    elif mode == 'd':
        message = decode(message)
        print(message)
    repeat = input('Would you like to encode/decode another message? (y/n): ')
    repeat = repeat.lower()
    while True:
        if repeat == 'y':
            mode, message = get_input()
            if mode == 'e':
                message = encode(message)
                print(message)
            elif mode == 'd':
                message = decode(message)
                print(message)
            repeat = input('Would you like to encode/decode another message? (y/n): ')
            repeat = repeat.lower()
            
        elif repeat == 'n':
            print('Thanks for using the program, goodbye!')
            break
        elif repeat != 'y':
            repeat = input('Would you like to encode/decode another message? (y/n): ')
            repeat = repeat.lower()
            continue


# Program execution begins here
if __name__ == '__main__':
    main()
