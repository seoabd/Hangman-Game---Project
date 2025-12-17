import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)

display_word = random_word

for char in random_word:
    display_word = display_word.replace(char, "_")

print(display_word)

word_underline = list(display_word)

maximum_guesses = 7

while "".join(word_underline) != random_word and maximum_guesses > 0:

    guess = input("Guess a letter: ").lower()

    if guess in random_word:

        for i, letter in enumerate(random_word):
            if letter == guess:
                word_underline[i] = guess

    else:
        maximum_guesses -= 1
        print(f"Sorry, the letter '{guess}' is not in the word. Please try again!")
        print(stages[maximum_guesses])
            
    print("".join(word_underline))

    if "".join(word_underline) == random_word:
        print(f"Congratulations, you guessed the right word.The word to be guessed was: {random_word}!")

    elif maximum_guesses <= 0:
        print("Sorry, you didn't guess the word! You lost!")
        break