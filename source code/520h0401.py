# -*- coding: utf-8 -*-
"""520H0401.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w7YSwQSkq_Fexa026ivOgD9vRhVWd3NJ
"""

#version 5
import collections
import re
import os
import sys
import time
import random
import string
from IPython.display import clear_output

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ETAOIN = 'etaoinshrdlcumwfgypbvkjxqz'
common_two_words_list = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']
common_three_words_list = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use']
common_four_letters_list = ['that', 'with', 'have', 'this', 'will', 'your', 'from', 'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time']

#create a dictionary list that contains all the words
def read_dictionary_file(links):
  with open(links) as file:
      dictionary_list = [w[:-1] for w in file.readlines()]
  return dictionary_list
#frequency analysis and mapping
def switch_crack(string):
    key = {}
    frequent_letters = collections.Counter(string).most_common()
    index = 0
    for letter in frequent_letters:
        if letter[0] in ALPHABET:
            key[ETAOIN[index]] = letter[0]
            index += 1
    return key
#used for replacing common word 2, 3 and 4
def replace_common_word(input_string, input_string_2, cipher_breaker, res3, common_word_list, number):
  token_1 = True
  while (token_1 == True):
    # os.system('cls')
    clear_output()
    time.sleep(1)
    sys.stdout.flush()
    print("REPLACE COMMON (%d) LETTERS WORDS:" % (number))
    print("Cipher Text:\n\t", input_string_2)
    user_input = str(input("What do you want to do? (1 for break cipher text/continue, 0 for cancel): "))
    if (user_input == '1'):
      print("\t>Common (%d) words:\n\t\t", common_word_list)
      print("\t>Cipher text and plain text:\n", "\t\t", input_string,"\n\t\t",input_string_2)
      print("\t>Cipher breaker:\n\t\t", cipher_breaker)
      # option, continue or end things
      token_2 = True
      while (token_2 == True):
        letter_input_2 = input("Enter letter in UPPERCASE: ")
        letter_input = input("Enter letter in lowercase: ")
        #action in here
        letter_input_2 = letter_input_2.strip().upper()[0]
        letter_input = letter_input.strip().lower()[0]
        if (len(letter_input)) > 1 or (len(letter_input_2) > 1):
          token_2 = True
        elif ((letter_input in cipher_breaker.values()) == True) or (letter_input_2 in cipher_breaker) == True:
          print("EXISTED")
          token_2 == True
        else:
          temp_string = '' + input_string_2
          temp_string = temp_string.replace(letter_input_2, letter_input)
          print("\t>Cipher text and plain text (REPLACED):\n", "\t\t", input_string,"\n\t\t", temp_string)
          # are you sure?
          user_option = str(input("> Are you sure you want to replace? (1 for YES, 0 for NO): "))
          if user_option == '1':
            input_string_2 = input_string_2.replace(letter_input_2, letter_input)
            cipher_breaker[letter_input_2] = letter_input
            res3 = [i.replace(letter_input_2, letter_input) for i in res3]
            token_2 = False
            break
          else:
            token_2 = True
    elif (user_input == '0'):
      token_1 = False
      break
    else:
      print("Wrong answer, please try again")
      token_1 = True
  return [input_string_2, cipher_breaker, res3]
#############################################################
def getmatches(matchstring, word_list):
  matchstring = matchstring.replace('-', '.')
  return [word for word in word_list if re.fullmatch(matchstring, word)]
def replace_uppercase_with_dash(input_string):
  s = '' + input_string
  for i in s:
    if i.isupper() == True:
      s = s.replace(i,'-')
  return s
def create_sub_list_dictionary_words(word, dictionary_list):
  word_replaced_dash = replace_uppercase_with_dash(word)
  result = getmatches(word_replaced_dash, dictionary_list)
  return result
def formula_1(input_string, input_string_2, cipher_breaker, res3, dictionary_list):
  clear_output()
  for word_index in range(len(res3)):
    clear_output()
    # print("the 1st:", res3[word_index],"\n", res3)
    sub_list = create_sub_list_dictionary_words(res3[word_index], dictionary_list)
    if ((res3[word_index].isupper() == False) and (res3[word_index].islower() == False)) and (len(sub_list) != 0):
      print(">Cipher text:\n\t", input_string_2)
      print(">This is your word:", res3[word_index], "\n>This is the suggested list:", sub_list)
      token_2 = True
      while (token_2 == True):
        uppercase_input = input("Enter letter in UPPERCASE: ")
        lowercase_input = input("Enter letter in lowercase: ")
        #action in here
        uppercase_input = uppercase_input.strip().upper()[0]
        lowercase_input = lowercase_input.strip().lower()[0]
        if (len(uppercase_input)) > 1 or (len(lowercase_input) > 1):
          token_2 = True
        elif ((lowercase_input in cipher_breaker.values()) == True) or (uppercase_input in cipher_breaker) == True:
          print("\t\t\t>>>EXISTED<<<")
          token_2 == True
        else:
          temp_string = '' + input_string_2
          temp_string = temp_string.replace(uppercase_input, lowercase_input)
          print("\t>Cipher text and plain text (REPLACED):\n", "\t\t", input_string,"\n\t\t", temp_string)
          # are you sure?
          user_option = str(input("> Are you sure you want to replace? (1 for YES, 0 for NO): "))
          if user_option == '1':
            input_string_2 = input_string_2.replace(uppercase_input, lowercase_input)
            cipher_breaker[uppercase_input] = lowercase_input
            res3 = [i.replace(uppercase_input, lowercase_input) for i in res3]
            token_2 = False
            break
          else:
            token_2 = True
  return [input_string_2, cipher_breaker, res3]
def decryption(input_string, dictionary_list):
  input_string_2 = '' + input_string
  #remove special character
  input_split = input_string.split(" ")
  input_remove_special_character = []
  for i in input_split:
    if " " in i or "." in i or "," in i or "!" in i or "?" in i:
      i = i.replace(i[-1], '')  
    input_remove_special_character.append(i)  
  #liệt kê hết tất cả các từ trong văn bản, chỉ xuất hiện 1 lần, sắp xếp theo chiều dài
  res3 = sorted(list(set(input_remove_special_character)), key = len)
  # print("res3:\n\t",res3)
  frequen_res = switch_crack(input_string)
  cipher_breaker = {}
  input_string_2 = input_string_2.replace(frequen_res["e"], 'e')
  res3 = [i.replace(frequen_res["e"], 'e') for i in res3]
  cipher_breaker[frequen_res["e"]] = 'e'
  input_string_2 = input_string_2.replace(frequen_res["t"], 't')
  res3 = [i.replace(frequen_res["t"], 't') for i in res3]
  cipher_breaker[frequen_res["t"]] = 't'
  input_string_2 = input_string_2.replace(frequen_res["a"], 'a')
  res3 = [i.replace(frequen_res["a"], 'a') for i in res3]
  cipher_breaker[frequen_res["a"]] = 'a'

  for i in res3:
    if "’" in i:
      # print(i[-1])
      input_string_2 = input_string_2.replace(i[-1], 's')
      temp = i[-1]
      res3 = [i.replace(temp, 's') for i in res3]
      cipher_breaker[i[-1]] = 's'

  common_1 = [i for i in res3 if len(i) == 1]
  for i in common_1:
    if i.islower() == False:
      temp = i
      input_string_2 = input_string_2.replace(temp, 'i')
      res3 = [i.replace(temp, 'i') for i in res3]
      cipher_breaker[temp] = 'i'
  ################################################
  result = replace_common_word(input_string, input_string_2, cipher_breaker, res3, common_two_words_list, 2)
  input_string_2 = result[0]
  cipher_breaker = result[1]
  res3 = result[2]
  ################################################
  result = replace_common_word(input_string, input_string_2, cipher_breaker, res3, common_three_words_list, 3)
  input_string_2 = result[0]
  cipher_breaker = result[1]
  res3 = result[2]
  ################################################
  result = replace_common_word(input_string, input_string_2, cipher_breaker, res3, common_four_letters_list, 4)
  input_string_2 = result[0]
  cipher_breaker = result[1]
  res3 = result[2]
  ################################################
  result = formula_1(input_string, input_string_2, cipher_breaker, res3, dictionary_list)
  return result
def cipher_breaker_string(cipher_breaker_dict):
  uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  uppercase_alphabet_2 = '' + uppercase_alphabet
  # uppercase_alphabet = uppercase_alphabet.replace('A', 'a')
  for key, values in cipher_breaker_dict.items():
    # print("key:", key, "\tvalues:", values)
    uppercase_alphabet = uppercase_alphabet.replace(key, values)
  res = uppercase_alphabet_2 + '\n' + uppercase_alphabet
  return res
#######################################################
def readFile(links):
  with open(links, "r") as file:
    input_string = file.read()
  file.closed
  return input_string
###########################################
def writeFile(links, data):
  with open(links, "w") as file:
    file.write(data)
  print("\t\t\t\t\t>>>COMPLETED WRITING TO FILE<<<")
  # print(file.read())
################################################################
#generate a random alphabet
def random_keyword_string (input_alphabet):
  return list_to_string(random.sample(input_alphabet, 26))
#generate an alphabet based on a keyword
def create_keyword_alphabet(input_keyword, alphabet):
  li = string_to_list("".join(dict.fromkeys(input_keyword)))
  l3 = [x for x in alphabet if x not in li]
  li.extend(l3)
  return list_to_string(li)
def list_to_string (input_string):
  return ''.join(item for item in input_string)
def string_to_list(input_string):
    li = []
    for i in input_string:
      li.append(i)
    return li
#replaced default_alphabet with keyword_alphabet
def monoalphabetic_substitution_encryption(keyword_alphabet, plaintext):
  cipher = ''
  for i in plaintext:
    if i in string.ascii_lowercase:
      index = ord(i) - ord('a')
      cipher = cipher + keyword_alphabet[index]
    else:
      cipher = cipher + i
  return cipher
def encryption(plain_text, keyword):
  default_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  if keyword != None:
    keyword_alphabet = create_keyword_alphabet(keyword, default_alphabet)
  else:
    keyword_alphabet = random_keyword_string(default_alphabet)
  result = monoalphabetic_substitution_encryption(keyword_alphabet, plain_text)
  return result.upper()
###################################################
input_plain_text_link = '/content/drive/MyDrive/Colab Notebooks/test folder/input_plain_text.txt'
encrypted_text_link = '/content/drive/MyDrive/Colab Notebooks/test folder/encrypted_text.txt'

keyword = 'zebraisstriped'
res = encryption(readFile(input_plain_text_link).lower(), keyword)
writeFile(encrypted_text_link, res)

##########################################################

input_cipher_text_link = '/content/drive/MyDrive/Colab Notebooks/test folder/input_cipher_text.txt'
english3_text_link = '/content/drive/MyDrive/Colab Notebooks/test folder/english3.txt'
decrypted_text_link = '/content/drive/MyDrive/Colab Notebooks/test folder/decrypted_text.txt'
ciher_breaker_link = '/content/drive/MyDrive/Colab Notebooks/test folder/cipher_breaker.txt'

res = decryption(readFile(input_cipher_text_link), read_dictionary_file(english3_text_link))
writeFile(decrypted_text_link, res[0])
writeFile(ciher_breaker_link, cipher_breaker_string(res[1]))

from google.colab import drive
drive.mount('/content/drive')