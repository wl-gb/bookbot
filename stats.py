def get_num_words(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    file_contents = file_contents.split()
    num_words = len(file_contents)
    return f"Found {num_words} total words"

def character_count(filepath):
  with open(filepath) as f:
    characters = {}
    file_contents = f.read()
    file_contents = file_contents.lower()
    for character in file_contents:
      if character not in characters:
        characters.update({character: 1})
      else:
        characters[character] += 1
    return(characters)

def report(filepath):
  total_words = get_num_words(filepath)
  characters = character_count(filepath)
  sorted_characters = []
  for character in characters:
    sorted_characters.append(f"{character}: {characters[character]}")
  sorted_characters.sort()
  formatted_report = f"============ BOOKBOT ============ \n Analyzing book found at {filepath}... \n ----------- Word Count ---------- \n {total_words} \n --------- Character Count ------- \n {sorted_characters} \n ============= END ==============="
  return #formatted_report

def report(filepath):
  total_words = get_num_words(filepath)
  characters = character_count(filepath)
  sorted_characters = []
  output_str = ""
  def sort_on(list):
    return list["num"]
  for character in characters:
    sorted_characters.append({"char": character, "num": characters[character]})
  sorted_characters.sort(reverse=True, key=sort_on)

  for dictionary in sorted_characters:
    output_str = output_str + (f"{dictionary["char"]}: {dictionary["num"]} \n")

  formatted_report = f"============ BOOKBOT ============ \n Analyzing book found at {filepath}... \n ----------- Word Count ---------- \n {total_words} \n --------- Character Count ------- \n {output_str} \n ============= END ==============="
  return formatted_report