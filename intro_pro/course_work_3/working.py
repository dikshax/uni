

morse_dic = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '.':'.-.-.-', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', '?':'..--..', '!':'-.-.--'}


message = 'HELLO WORLD'

def encode(message):
    cipher =''

    for letter in message:
    	if letter != ' ':
        	cipher += morse_dic[letter] + ' '
        else:
        	cipher += '   '
    return cipher


work = encode(message)
print(work)

message = '.... . .-.. .-.. ---    .-- --- .-. .-.. -..'
def decode(message):
	decipher = ''

	words = message.split('   ')
	for morse_word in words:
		chars = morse_word.split()
		for char in chars:
			for key, value in morse_dic.items():
				if char == value:
					decipher += key
		decipher += ' '
	return decipher
		

work = decode(message)
print(work)