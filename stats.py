def count_words(text):
  word_list = len(text.split())
  return word_list

def count_characters(text):
  lower_case = text.lower()
  # print(lower_case)
  char_frequency = {}

  for char in lower_case:
    if char in char_frequency:
      char_frequency[char] +=1
    else:
      char_frequency[char] = 1
  
  return char_frequency


def sort_on(d):
  return d["num"]

def sorted_list(num_chars_dict):
  individual_dicts = []
  for ch in num_chars_dict:
    individual_dicts.append({"char": ch, "num": num_chars_dict[ch]})
  individual_dicts.sort(reverse=True, key=sort_on)
  return individual_dicts