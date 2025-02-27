import random

welcome_message = "Welcome to Guess the Glass"
ball_position = random.randint(1, 10)

continue_game = True

while continue_game:
    print("=========================================")
    print(f"====== {welcome_message} =======")
    print("=========================================")

    player_name = input("Please enter your name: ")
    print("[1] [2] [3] [4] [5] [6] [7] [8] [9] [10]")
    print(f"Hello {player_name}, please choose which glass you are thinking of a number between 1 and 10")

    guess = input("Please guess a number or type 'exit' to quit: ")

    match guess.lower():
        case 'exit':
            continue_game = False
        case _ if int(guess) == ball_position:
            print(f"You got it! The Ball Position is on {ball_position} and You guessed {guess}")
        case _:
            print(f"You did not get it :( The Ball Position is on {ball_position} and You guessed {guess}")
    
    print("=========================================")
