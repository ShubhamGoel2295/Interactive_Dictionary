import json
import difflib # lib to compare text
from difflib import get_close_matches

data= json.load(open(r'C:\Users\egoeshu\Desktop\testingdoc\Python Mega Projects\Interactive Dictionary_app1\data.json'))

def translate(w):
    w= w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))> 0: # matching word with keys. len used because if matches found moret han 1 thwn only cond. is true. here cutoff is there 0.6 which using while matching
        yn= input(f"Did you mean {get_close_matches(w, data.keys())[0]} ?. Enter y for yes and n for no: ") #asking for rainn with rain
        if yn =='y':
            return data[get_close_matches(w, data.keys())[0]] # fetching the accurate key after matching rainn with rain
        elif yn=='n':
            return 'The word does not exist. Thank You'
        else:
            return 'We didnt understand your query. Bye'
    else:
        return 'The word does not exist. Please double check it'


word= input("enter the word to find meaning: ")
output= translate(word)
if type(output)== list:
    print('\n'.join(output))
else:
    print(output)