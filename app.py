import json
from difflib import get_close_matches
Data = json.load(open('data.json'))

def Dictionary(w):
    w = w.lower()
    if w in Data:
        return Data[w]
    elif len(get_close_matches(w,Data.keys())) > 0 :
        yn = input('Did you mean %s instead?\nEnter y for yes and n for no: '% get_close_matches(w,Data.keys())[0])
        if yn.lower() == "y":
            return Data[get_close_matches(w,Data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist"

    else:
        return 'The word does not exist.'


word = input('Enter a word: ')

out_put = Dictionary(word)
if type(out_put) == list:
    for item in out_put:
        print(item)
else:
    print(out_put)
