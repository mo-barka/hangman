import random
import sys

list_words = ['honour', 'object', 'sustained', 'reasonable']
word_choice = random.choice(list_words)
hidden_word = list('-' * len(word_choice))
used_letters = []
lives = 8

#menu
print("H A N G M A N")
authorization = ''
while authorization != 'ok':
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        authorization = 'ok'
    elif menu == 'exit':
        sys.exit()
    else:
        continue

 #game
while lives > 0:
    print('\n' + ''.join(hidden_word))
    if '-' not in hidden_word:
        print('Congratulations, you guessed the word correctly!', '\U0001F389' * 30, sep='\n')
        break
    if lives == 8:
        print('You have ' + str(lives) + ' lives')
    letter = input('Input a letter: ')
    if letter.isupper() or not letter.isalpha():
        print('You must insert a lowercase letter')
    if len(letter) != 1:
        print('You should input a single letter')
        continue
    if letter in word_choice and letter not in hidden_word:
        for i in range(len(word_choice)):
            if word_choice[i] == letter:
                hidden_word[i] = letter
    elif letter in word_choice and letter in hidden_word or letter in used_letters:
        print('You already typed this letter')
    elif letter.islower() and letter.isalpha():
        print('No such letter in the word')
        lives -= 1
        print('You now have ' + str(lives) + ' lives left')
    used_letters.append(letter)
else:
    print('You were executed :(')
