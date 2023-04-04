import sys


def alpha_to_morse(sentence):
    # Morse alphabete char map
    morse_alphabet = {
        "A": "*-",
        "B": "-***",
        "C": "-*-*",
        "D": "-**",
        "E": "*",
        "F": "**-*",
        "G": "--*",
        "H": "****",
        "I": "**",
        "J": "*---",
        "K": "-*-",
        "L": "*-**",
        "M": "--",
        "N": "-*",
        "O": "---",
        "P": "*--*",
        "Q": "--*-",
        "R": "*-*",
        "S": "***",
        "T": "-",
        "U": "**-",
        "V": "***-",
        "W": "*--",
        "X": "-**-",
        "Y": "-*--",
        "Z": "--**",
        "1": "*----",
        "2": "**---",
        "3": "***--",
        "4": "****-",
        "5": "*****",
        "6": "-****",
        "7": "--***",
        "8": "---**",
        "9": "----*",
        "0": "-----",
        ".": "*-*-*-",
        ",": "--**--",
        ":": "---***",
        "?": "**--**",
        "'": "*----*",
        "()": "	-*--*-",
        " ": " "
    }
    try:
        # Convert each char of a given sentence
        morse = [morse_alphabet[letter] for letter in sentence]
    except KeyError:
        print("Symbol not recognized. Try again...")
        return main()
    return ' '.join(morse)


def main():
    while True:
        # Convert sentence to morse
        morse_sentence = alpha_to_morse(input("Sentence: ").upper())
        print("\n" + morse_sentence + "\n")

        app_status = ""

        # Validate user input for app status
        while app_status not in ["Y", "YES", "N", "NO"]:
            app_status = input("Would you like to continue? (Y/N): ").upper()

        if app_status in ["Y", "YES"]:
            continue
        else:
            return False


if __name__ == "__main__":
    main()
