import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def write():
    word_user = input("Typed out a word:").upper()

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    list_code = []
    try:
        list_code = [data_dic[letter] for letter in word_user]
    except KeyError:
        print("Please only letter in the input")
    else:
        print(list_code)
    finally:
        write()

write()
