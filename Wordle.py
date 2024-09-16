word = "great"

# colors for printing 
default = '\033[0m'
green = '\033[92m'
yellow = '\033[32m'

# function to gernate hint with correct letter colors
def generate_hint(guess):
    color = default
    hint = ""
    for i in range(5):
        if(guess[i] == word [i]):
            color = green
        elif guess[i] in word:
            color = yellow 
        else:
            color = default
            # adds letter with correct color to hint word
        hint = hint + color + guess[i] + default
    return hint 

# function that loops 6 times once for each guess
def game_loop():
    user_guess = ""
    for i in range(6):
        user_guess = input("give us a guess: ")
        print(generate_hint(user_guess))
        if user_guess == word:
            print("congradulations!!!")
            break 

game_loop()