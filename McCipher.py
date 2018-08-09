Mcode = { 'A': '.-', 'B': '-...', 'C': '-.-.', 
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
     	'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', 
        
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        '.': '.-.-.-', ':': '---...', ',': '--..--',
        ';': '-.-.-.', '?': '..--..', '=': '-...-',
        "'": '.----.', '/': '-..-.', '!': '-.-.--',
        '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '(': '-.--.', ')': '-.--.-', '$': '...-..-',
        '&': '.-...', '@': '.--.-.', '+': '.-.-.', 
        ' ': '' }

text = {v: k for k, v in Mcode.iteritems()}

Ccode = { '.-': '1A', '-...': 'A3', '-.-.': 'A1A1',
        '-..': 'A2', '.': '1', '..-.': '2A1',
        '--.': 'B1', '....': '4', '..': '2',
        '.---': '1C', '-.-': 'A1A', '.-..': '1A2',
        '--': 'B', '-.': 'A1', '---': 'C',
        '.--.': '1B1', '--.-': 'B1A', '.-.': '1A1',
     	'...': '3', '-': 'A', '..-': '2A',
        '...-': '3A', '.--': '1B', '-..-': 'A2A',
        '-.--': 'A1B', '--..': 'B2', 
        
        '-----': 'E', '.----': '1D', '..---': '2C',
        '...--': '3B', '....-': '4A', '.....': '5',
        '-....': 'A4', '--...': 'B3', '---..': 'C2',
        '----.': 'D1',

        '.-.-.-': '1A1A1A', '---...': 'C3', '--..--': 'B2B',
        '-.-.-.': 'A1A1A1', '..--..': '2B2', '-...-': 'A3A',
        '.----.': '1D1', '-..-.': 'A2A1', '-.-.--': 'A1A1B',
        '-....-': 'A4A', '..--.-': '2B1A', '.-..-.': '1A2A1',
        '-.--.': 'A1B1', '-.--.-': 'A1B1A', '...-..-': '3A2A',
        '.-...': '1A3', '.--.-.': '1B1A1', '.-.-.': '1A1A1', 
        ' ': '', '  ': ' ' }

Dcode = {v: k for k, v in Ccode.iteritems()}


def morse():
    msg = raw_input('MESSAGE: ')
    
    if not msg:
        print "You need to enter a message!"
        msg

    nmsg = msg.split(' ')

    print "\nOptions:"
    print "1. Text to Morse Code"
    print "2. Morse Code to text"
    choice = raw_input(">> ")

    if choice == "1":
        for char in msg:
            print Mcode[char.upper()],

    elif choice == "2":
        for char in nmsg:
            if char in text:
                print text[char],
            else:
                print "<CNF>"


def cipher():
    msg = raw_input('MESSAGE: ')
    
    if not msg:
        print "You need to enter a message!"
        msg

    nmsg = msg.split(' ')

    print "\nOptions:"
    print "1. Text to Cipher"
    print "2. Cipher to text"
    choice = raw_input(">> ")

    if choice == "1":
        for char in msg:
	        print Ccode[Mcode[char.upper()]],



    elif choice == "2":
        for char in nmsg:
            if char in Dcode:
	            mor = Dcode[char],
            else:
                print "<CNF>"
        
            for char in mor:
                if char in text:
                    print text[char],


def main():
    while True:
        print "\nOptions:"
        print "1. Morse Code"
        print "2. Cipher"

        choice = raw_input(">> ")

        if choice == "1":
            morse()
        elif choice == "2":
            cipher()



if __name__ == "__main__":
	main()