import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def search_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        return ("Did you mean ' %s ' instead?" % get_close_matches(w, data.keys())[0])
    else:
        return "The word doesn't exist. Please double check it."

