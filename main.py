import pandas

csv = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in csv.iterrows()}
print(dict)

def generate_phonetic():
    user_input = input("Enter a word: ")
    lis = list(user_input.upper())
    try:
        phonetic_list = [dict[letter] for letter in lis]

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()

