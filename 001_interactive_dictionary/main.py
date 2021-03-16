import json
from difflib import get_close_matches # (word, possibilites(dic, list, data), n, ratio)

data = json.load(open("data.json"))


def translate(word):
    # Converting the word to lower case
    word = word.lower()

    # check if the word exists
    if word in data:
        return data[word]

    # Check if the word [in title form] exists
    elif word.title() in data:
        return data[word.title()]

    # Check if the matches of the word exist
    elif len(get_close_matches(word, data.keys())) > 0:
        msg01 = input("Did you mean %s instead? (y/n) " %
                      get_close_matches(word, data.keys())[0])

        if msg01.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]

        elif msg01.lower() == "n":
            return "The word doesn't exist."

    else:
        return "The word doesn't exist."


word = input("Enter a word:")

output = translate(word)

# preventing the output of the list 
# to be printed for strings if an error happens
if type(output) == list:
    c = 1
    for item in output:
        print(f"{c} : {item}")
        c += 1
else:
    print(output)
