import json
import difflib
from difflib import get_close_matches

def translate_text(word, data):
    if word in data:
        return data[word]
    else:
        possible_words = get_close_matches(word,data.keys(),n=5,cutoff = 0.8)
        print(possible_words)
        if len(possible_words) != 0:
            high_accurate_word = possible_words[0]
            print("Did You Mean \"{}\"".format(high_accurate_word))
            print(end="\n")
            ask = input("If \"Yes\" Enter \"Y\" otherwise Enter \"N\": ")
            if ask == "Y":
                return data[high_accurate_word]
            for i in range(1,len(possible_words)+1): print(i, possible_words[i-1])
            ask_again = input("If you find any word at above list then enter the sequence number otherwise Enter \"N\": ")
            try:
                ask_again = int(ask_again)
                return data[possible_words[ask_again-1]]
            except IndexError:
                return "Invalid Index"
            except  ValueError:
                return "No word Found"
        return "Incorrect Word Entry..Please Double Check it again."


def main():
    data = json.load(open("C:\\Users\\ribhu\\OneDrive\\Desktop\\Python\\PYTHON_ENGLISH_THESAURUS\\data.json"))
    word = input("Enter a word to search for the Meaning: ")
    meaning = translate_text(word.lower(),data)
    if isinstance(meaning,list):
        print(*meaning, sep = " \n")
    else:
        print(meaning)
    
if __name__ == "__main__":
    main()
