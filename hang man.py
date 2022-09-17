# Hi

print('H A N G M A N')
import random
win = 0
loss = 0
# While true, if input == play break out of the loop and start the game
while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu == 'results':
        print('You won: '+ str(win) + ' times.')
        print('You lost: '+ str(loss) + ' times.')
    if menu == 'exit':
        exit()
    if menu == 'play':
        break
def game():
    attempt_count = 8
    word = random.choice(['python', 'java', 'swift', 'javascript'])
    hint = list('-' * (len(word)))
    # while attempts count dosen't equal zero do all this stuff

    while attempt_count != 0:
    
# printing the 'Input a letter:' and the hint with all the breaks and stuff

        print('\n' + str(("".join(hint))) + '\n' + 'Input a letter: ')
        letter_guess = input()
        # Checking wether, lowercase, not in word, already guessed letter and non english letters.
        if len(letter_guess) >= 2 or len(letter_guess) <= 0:
            print('Please, input a single letter.')
        
        elif letter_guess.isupper() or letter_guess.isalpha() == False:
            print('Please, enter a lowercase letter from the English alphabet.')
    
        elif letter_guess not in word:
            print("That letter doesn't appear in the word.")
            attempt_count += -1
        
        elif letter_guess in str(("".join(hint))):
            print("You've already guessed this letter.")
    
    # if the guess is in the word, for each letter between position zero and length of word check if 
    # the letter guess is in a position of the word, change the hint with the word they guessed (sorry if bad explanation)
    
        elif letter_guess in word:
            for i in range(0, len(word)):
                if letter_guess == word[i]:
                    hint[i] = letter_guess

        # if attempts is equal to 0 print 'Thanks for playing!' break from the loop(works)      
        if attempt_count == 0:
            print('You lost!')
            global loss
            global win
            loss += 1
            while True:
                menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
                if menu == 'results':
                    print('You won: '+ str(win) + ' times.')
                    print('You lost: '+ str(loss) + ' times.')
                if menu == 'exit':
                    exit()
                if menu == 'play':
                    attempt_count = 8
                    game()
                    break
    
        if str(("".join(hint))) == word:
            print(str(("".join(hint))))
            print('You guessed the word ' + str(("".join(hint))) + '!')
            print('You survived!')
            win += 1
            while True:
                menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
                if menu == 'results':
                    print('You won: '+ str(win) + ' times.')
                    print('You lost: '+ str(loss) + ' times.')
                if menu == 'exit':
                    exit()
                if menu == 'play':
                    attempt_count = 8
                    game()
                    break
game()
