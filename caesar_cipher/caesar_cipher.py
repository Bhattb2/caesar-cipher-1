import nltk
nltk.download('words')
from nltk.corpus import words

def encrypt(text, key):
  '''Takes in a string of letters (non alpha characters and white spaces are ignored) along with a numeric shift and returns a string'''
  if not isinstance(key,int):
    raise ValueError("The key argument has to be an integer")
  if not isinstance(text,str):
    raise ValueError("Please enter the text argument as a string")
  word_list = words.words()
  alpha_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
  new_string = ""

  def encrypt_char(num):
    shift = (num+key) % len(alpha_list)
    new_char = alpha_list[shift]
    return new_char

  for char in text:
    if char.lower() in alpha_list:
      num = alpha_list.index(char.lower())
      new_char= encrypt_char(num)
      if char.isupper():
        new_string+=str(new_char.upper())
      else:
        new_string+=str(new_char)
    else:
      new_string+=str(char)
  return new_string    

def decrypt(text,key):
  '''Takes in a string of encrypted text (non alpha characters and white spaces are ignored) along with a numeric key and returns a string'''
  if not isinstance(key,int):
    raise ValueError("The key argument has to be an integer")
  if not isinstance(text,str):
    raise ValueError("Please enter the text argument as a string")
  return encrypt(text,-key)


def break_code(text):
  if not isinstance(text,str):
    raise ValueError("Please enter the text argument as a string") 
  alpha_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
  word_list = words.words()
  for key in range(26):
    counter = 0
    string = encrypt(text, key)
    string_list = [j for j in string.split(" ")]
    for word in string_list:
      if word in word_list:
        counter += 1
      elif word[-1] == "s":
        l = len(word)
        if word[0:(l-1)] in word_list:
          counter += 1
    if counter/len(string_list)>0.5:
      return string


if __name__ == "__main__":
  # prints 236736
  print(encrypt("Gb trg gb gur bgure fvqr!",13))
