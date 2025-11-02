def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    og = text.lower()
    char_dict = {}
    x = og.split()
    for word in x:
        for char in word:
            if char in char_dict:
                char_dict[char]+=1
            else:
                char_dict[char]=1
    return char_dict

def sort_on(items):
    return items['num']

def sort_count (char_dict):
    rows = []
    for char, count in char_dict.items():
        if char.isalpha() == True:
            rows.append({"char": char, "num": count})
    rows.sort(key=sort_on, reverse=True)
    return rows
        
    
