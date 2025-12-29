from stats import get_num_words, character_count, report
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  #print(get_book_text(sys.argv[1]))
  #print(get_num_words(sys.argv[1]))
  #print(character_count(sys.argv[1]))
  print(report(sys.argv[1]))
main()