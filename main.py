from stats import number_of_words, character_count,sorted_dictionary
import sys
def get_string(filepath):
    with open(filepath) as f:
        return_string=f.read()
    return return_string 
def main():
    try:
        print(f"========== BOOKBOT ==============\nAnalyzing book found at {sys.argv[1]}...\n---------Word ount ----------\n")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    string=get_string(sys.argv[1])
    print(f"Found {number_of_words(string)} total words\n-----------Character Count -------------\n" )
    array=sorted_dictionary(character_count(string)) 
    for i in array:
        if i["char"].isalpha()==True:
            char=i["char"]
            count=i["count"]
            print(f"{char}: {count}") 
main() 