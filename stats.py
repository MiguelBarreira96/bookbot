def num_words(text):
    Words = text.split()
    numWords = len(Words)
    return numWords

def letter_count(text):
    count = {}
    new_text = text.lower()
    for c in new_text:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1


    return count 

def sort_on(dict):
    return dict["num"]

def sort_in(dict):
    
    new_list = []
    for k, v in dict.items():
        if k.isalpha():
            new_dir =  {"char":k, "num":v}
            new_list.append(new_dir)
    new_list.sort(reverse=True, key=sort_on)
    return new_list