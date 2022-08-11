import random

# word list
words = ['python', 'java', 'swift', 'javascript']

print("H A N G M A N")  # start banner
accepted_input = ["play", "results", "exit"]
total_wins = 0
total_loses = 0

# main menu of the game
while True:

    # random word from the list
    right_word = words[random.randint(0,3)]

    # reaviling the word with hyphens
    hyphenated_word = list(("-" * (len(right_word))))
    suggested_letters = []

    user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if user_input not in accepted_input:
        continue
    elif user_input == "results":
        print(f"You won: {total_wins} times")
        print(f"You lost: {total_loses} times")
        continue
    elif user_input == "exit":
        break

    # real game begins
    attemps = 8
    while attemps >= 1:
        # if the word has been guessed break out of the loop
        if "-" not in hyphenated_word:
            break
        
        print("".join(hyphenated_word))
        letter = input("Input a letter: ")  # ask for a letter input 

        # error checking on the letter
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in suggested_letters:
            print("You've already guessed this letter.")

        # the letter does not exist in the word
        elif letter not in right_word: 
            print("That letter doesn't appear in the word.")
            attemps -= 1
        else:
            suggested_letters.append(letter)
        # loop for unrevealing the word in hyphens
        for i in range(0, len(hyphenated_word)):
            if letter == right_word[i]:
                hyphenated_word[i] = letter

    # end of program
    if '-' in hyphenated_word:
        print("You lost!")
        total_loses += 1
    else:
        print(right_word)
        print(f"You guessed the word {right_word}!")
        print("You survived!")
        total_wins += 1
