#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0,2)]

print(f'Pssst, the solution is {chosen_word}.')

#Set up a display showing letter slots hidden
display=[]
for chars in range(len(chosen_word)):
  display.append("_")

guess = (input("Guess a letter: ")).lower()

#Compare user guess with letters, reveal found letters in disp.

for letter in range(len(chosen_word)):
  if guess == chosen_word[letter]:
    display[letter] = chosen_word[letter]

print(display)