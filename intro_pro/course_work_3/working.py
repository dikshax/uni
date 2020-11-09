

morse_dic = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '.':'.-.-.-', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', '?':'..--..', '!':'-.-.--'}


message = 'T'

def encode(message):
    final_code =''

    for letter in message:
        final_code += morse_dic[letter]
    return final_code


work = encode(message)
print(work)


message = '-'
def decode(message):
    final_string = ''

    for chractor in message:
        final_string += morse_dic[chractor]

    return final_string


work = decode(message)
print(work)
