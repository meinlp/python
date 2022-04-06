import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}


def generate_phonetic():
    word = input("Which word do you want to convert?\n").upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
