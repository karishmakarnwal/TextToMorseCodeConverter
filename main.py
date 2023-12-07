
morse_code_dict = {'a': '. –', 'b': '– . . .', 'c': '– . – .', 'd': '– . .',
                   'e': '.', 'f': '. . – .', 'g': '– – .', 'h': '. . . .',
                   'i': '. .', 'j': '. – – –', 'k': '– . –', 'l': '. – . .',
                   'm': '– –', 'n': '– .', 'o': '– – –', 'p': '. – – .',
                   'q': '– – . –', 'r': '. – .', 's': '. . .', 't': '–',
                   'u': '. . –', 'v': '. . . –', 'w': '. – –', 'x': '– . . –',
                   'y': '– . – –', 'z': '– – . .', '1': '. – – – –', '2': '. . – – –',
                   '3': '. . . – –', '4': '. . . . –', '5': '. . . . .', '6': '– . . . .',
                   '7': '– – . . .', '8': '– – – . .', '9': '– – – – .', '0': '– – – – –',
                   ' ': '       ', '.': '. – . – . –', ',': '– – . . – –', '?': '. . – – . .',
                   '\'': '. – – – – .', '!': '– . – . – –', '\\/': '– . . – .', '(': '– . – – .',
                   ')': '– . – – . –', '&': '. – . . .', ':': '– – – . . .', ';': '– . – . – .',
                   '=': '– . . . –', '+': '. – . – .', '-': '– . . . . –', '_': '. . – – . –',
                   '\"': '. – . . – .', '$': '. . . – . . –', '@': '. – – . – .'}

# the space between letters is 3 units
# the space between words is 7 units


def text_to_morse_code(entered_text):
    morse_code = ""
    space_between_letters = '   '
    count = 0

    for char in entered_text:
        try:
            morse_code += morse_code_dict[char.lower()]
        except KeyError as ke:
            print('Key Not Found in Morse Code Dictionary:', ke)
        finally:
            if len(entered_text) - 1 > count:
                morse_code += space_between_letters

            count += 1

    print(f'The converted morse code is {morse_code}')


should_end = False
while not should_end:
    text = input("Type text to convert to morse code:\n")

    text_to_morse_code(text)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
