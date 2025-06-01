from stats import *
import sys

if len(sys.argv) == 2:

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents
        return None



    file_contents = get_book_text(sys.argv[1])
    num = num_words(file_contents)
    count_file = letter_count(file_contents)
    final_list = sort_in(count_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in final_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)