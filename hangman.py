import random
import string

words = ['apple', 'banana', 'mango', 'orange', 'peach']
secret_word = random.choice(words)
player_word = []
letters = list(string.ascii_lowercase)
guessed_letters = []


def show_board():
    player_letters = ' '.join(letters)
    print(f'\nPlayable letters: {player_letters}')
    guessed = ' '.join(guessed_letters)
    print(f'NOT playable: {guessed}')


def create_word():
    print('\nYour secret word is: \n')
    for letter in secret_word:
        letter = '_'
        player_word.append(letter)
    print(' '.join(player_word))
    show_board()


def run():
    create_word()
    count = 0
    while count < 8:
        try:
            player_choice = input('\nPlease enter a letter: ') 
            for ind, letter in enumerate(list(secret_word)):
                if player_choice in letter:
                    player_word[ind] = letter
            letters.remove(player_choice)
            guessed_letters.append(player_choice)
            print(' '.join(player_word))
            show_board()
            count += 1
        except:
            print('Please try a different letter.')
        word = ''.join(player_word)
        if str(word) == str(secret_word):
            print(f'\nYou win the secret word was {secret_word}.\n')
            break
        elif count < 8:
            continue
        else:
            print(f'\nYou lose the secret word was {secret_word}.\n')


run()
