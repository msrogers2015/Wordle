#!/usr/bin/env python3
import colorama
import random
from colorama import Back as b
from data import words

colorama.init(autoreset=True)
guess = ''
word = random.choice(words)
guess_list = []

while guess != word:
  guess = input('Guess the word: ')
  for letter in range(5):
    if guess[letter] == word[letter]:
      guess_list.append(b.GREEN + guess[letter])
    elif guess[letter] in word:
      guess_list.append(b.YELLOW + guess[letter])
    else:
      guess_list.append(b.RED + guess[letter])
  print(''.join(guess_list))
  guess_list = []
  
print('Congrats! You won!')
