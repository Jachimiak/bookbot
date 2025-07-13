import sys
from stats import count_words
from stats import count_characters
from stats import sorted_list




def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_location = sys.argv[1]
  whole_text = get_book_text(book_location)
  
  # print(whole_text)
  total_words = count_words(whole_text)
  characters = (count_characters(whole_text))
  sorted_characters = sorted_list(characters)
  print_report(book_location, total_words, sorted_characters)

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents


def print_report(book_location, total_words, sorted_characters):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_location}...")
  print("----------- Word Count ----------")
  print(f"Found {total_words} total words")
  print("--------- Character Count -------")
  for item in sorted_characters:
    if not item["char"].isalpha():
      continue
    print(f"{item['char']}: {item['num']}")

  print("============= END ===============")

if __name__ == '__main__':
  main()
