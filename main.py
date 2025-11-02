import stats
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    return book_text


    
if __name__ == "__main__":
    try:
        characters = main()
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    counters = stats.char_count(characters)
    words = stats.word_count(characters)
    sorted_list = stats.sort_count(counters)

    
    print(f'''============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------''')
    print(f'Found {words} total words')
    print('''--------- Character Count -------''')
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")