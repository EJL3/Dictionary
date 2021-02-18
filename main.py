import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Whats the word you wanna look ? : ")
word = word.lower()
def getMeaning(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print("did you mean %s enter Y (yes) or enter N (no) :"%close_match)
        choice = input()
        choice=choice.lower()
        if(choice == 'y'):
            return data[close_match]
        else:
            return "word is not Availible please try something else :("
out = str(getMeaning(word))

print("\n"+out+"\n")

