from random import choice                                                      #imports method:choice from module:random 

lives = 7                                                                      #lives user has for game
letters = []                                                                   #list 
words = open('word_list.txt').read().split()                                   #gets words from txt file
word = choice(words)                                                           #selects word from words as string

for i in range(len(word)):      
  letters.append(word[i])                                                      #change string to list 

stars = ['*' for _ in letters]                                                 #changes lists to *

while lives > 0:                                                               #create while loop for game rules
  guess = input('{} Please enter your next guess: ' .format(''.join(stars)))   #stars + user instruction

  if guess in letters:                                                         #if guess correct, letters change * into guess
    for i in range(len(word)):
      if letters[i] == guess:
        stars[i] = guess
  else: 
    lives = lives - 1                                                          #if guess incorrect, reduce lives by 1

  if '*' not in stars:                                                         #win condition
    print('congratulations you win')                        
    break                                                                      #end the while loop

if lives == 0:                                                                 #lose condition
  print('you lose')

  #code written by Christopher Ong 30137388 
