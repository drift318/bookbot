import stats

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    return book_text


    
if __name__ == "__main__":
    characters = main()  
    counters = stats.char_count(characters)
    words = stats.word_count(characters)
    sorted_list = stats.sort_count(counters)

    
    print('''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
    print(f'Found {words} total words')
    print('''--------- Character Count -------''')
    for i in sorted_list:
        print(f'{i['char']}: {i['num']}')