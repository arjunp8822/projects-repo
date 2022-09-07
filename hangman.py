import random
import string

words = ['arjun', 'anita', 'birthday']

def select_random_word(word_list):
    random_word = random.choice(word_list)
    return random_word

all_letters = string.ascii_letters.lower()

def hangman():
    word = select_random_word(words)
    word_letters = set(word) # unique letters in word
    alphabet = set(string.ascii_letters.lower()) # string of all letters in alphabet
    used_letters = set() # unique letters already used
    
    hangman = 'HANGMAN'
    lives = ''
    
    while len(word_letters) > 0 and lives != 'HANGMAN':
        
        print(f'You have used the following letters: ', ' '.join(used_letters))
        display_word = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(display_word))
        print('Lives left: ', ' '.join(lives))
        
        guess_letter = input('Guess a letter: ').lower()
        
        if guess_letter in alphabet - used_letters:
            used_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
            else:
                life_letter = hangman[0]
                hangman = hangman[1:]
                lives = lives + life_letter
                
        elif guess_letter in used_letters:
            print('You have already guessed this letter.')
            
        else:
            print('Invalid character, please try again.')

    if lives == 'HANGMAN':
        print("You lost :(")
    else:
        print("You won!")

hangman()