def main(file):
    total = 0
    with open(file) as f:
        file_content = f.read()
        for i in file_content.split():
            total += 1
    return total

def letter_count(book):
    dict_count ={}
    with open(book) as f:
        text = f.read().lower()
        for i in text:
            if i not in dict_count:
                dict_count[i]= 1
            elif i in dict_count:
                dict_count[i] +=1
            else:
                pass
    return dict_count

def report (count, dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document \n")
    for i in dictionary:
        if i.isalpha()==True:
            print(f"The '{i}' character was found {dictionary[i]} times")
        else:
            pass


if __name__== "__main__":
    file = (r"/Users/michaeltrusty/workspace/github.com/books/frankenstein.txt")
    word_count=main(file)
    character_count=letter_count(file)
    report(word_count,character_count)