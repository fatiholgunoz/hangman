import random
import hangman_art
import hangman_words
from replit import clear

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(hangman_art.logo)
chosen_word = hangman_words.word_list[random.randint(0,213)]
letter_count = len(chosen_word)

#print(f'Pssst, the solution is {chosen_word}.')

#Set up a display showing letter slots hidden
display=[]
for chars in range(letter_count):
  display.append("_")

#Compare user guess with letters, reveal found letters in disp.
#Repeat until no hidden letters left
  
hidden_letters = letter_count
lives = 6

while hidden_letters > 0 and lives > 0:
  guess = (input("Guess a letter: ")).lower()
  clear()
  for letter in range(letter_count):
    if guess in display[letter]:
      print("This letter is already found!")
    elif guess == chosen_word[letter]:
      display[letter] = chosen_word[letter]
      hidden_letters = hidden_letters - 1 
    
  if guess not in chosen_word:
    print(f"The letter '{guess}' is not in the word. ")
    lives = lives - 1  
    
  print(f"{' '.join(display)}")
  print(f"\n{lives} lives left.")
  print(hangman_art.stages[lives])
  
  if hidden_letters == 0:
    print("\nYou win!")
  elif lives == 0:
    print("\nYou lose!")
    print(f"The word was {chosen_word}.")

