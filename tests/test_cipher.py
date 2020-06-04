import pytest
from caesar_cipher.caesar_cipher import encrypt,decrypt, break_code

def test_encrypt_import():
  assert encrypt

def test_decrypt_import():
  assert decrypt

def test_break_code_import():
  assert decrypt

def test_encrypt_shift_raise_integer_valueerror():
  with pytest.raises (ValueError):
    assert encrypt("hi", "hi")
  
def test_encrypt_shift_raise_string_valueerror():
  with pytest.raises (ValueError):
    assert encrypt(4, 3)

def test_decrypt_shift_raise_integer_valueerror():
  with pytest.raises (ValueError):
    assert decrypt("hi", "hi")
  
def test_decrypt_shift_raise_string_valueerror():
  with pytest.raises (ValueError):
    assert decrypt(4, 3)

def test_break_code_raise_string_valueerror():
  with pytest.raises (ValueError):
    assert break_code(4)

def test_encrypt_lower_case():
  actual = encrypt("cats", 3)
  expected = "fdwv"
  assert actual == expected

def test_encrypt_upper_and_lower_case():
  actual = encrypt("CatS", 3)
  expected = "FdwV"
  assert actual == expected

def test_encrypt_upper_lower_nonAlpha():
  actual = encrypt("CatS & DogS!@%", 3)
  expected = "FdwV & GrjV!@%"
  assert actual == expected

def test_decrypt_with_key_lower():
  actual = decrypt("fdwv", 3)
  expected = "cats"
  assert actual == expected

def test_decrypt_upper_and_lower_case():
  actual = decrypt("FdwV", 3)
  expected = "CatS"
  assert actual == expected

def test_decrypt_upper_lower_nonAlpha():
  actual = decrypt("FdwV & GrjV!@%", 3)
  expected = "CatS & DogS!@%"
  assert actual == expected

def test_break_code_correct_word():
  actual = break_code("cat")
  expected = "cat"
  assert actual == expected

def test_break_code_correct_word():
  actual = break_code("xghhozy")
  expected = "rabbits"
  assert actual == expected

def test_break_code_correct_sentence():
  actual = break_code("S vyfo rkwc")
  expected = "I love hams"
  assert actual == expected

def test_break_code_correct_sentence():
  actual = break_code("Oz cgy znk hkyz ul zosky, oz cgy znk cuxyz ul zosky.")
  expected = "It was the best of times, it was the worst of times."
  assert actual == expected