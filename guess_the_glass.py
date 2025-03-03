import random

welcome_message = "Welcome to Guess the Glass"
ball_position = random.randint(1, 10)

continue_game = True
glasses_print = "[]"
glasses = [glasses_print] * 4

# print(f"glasses {glasses}")

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"my_list {my_list}")
# my_list.sort()
# print(f"my_list sorted {my_list}")
new_list = sorted(my_list)
print(f"new_list {new_list}")
new_list[2] = 10
print(f"new_list after modifying {new_list}")
print(f"my_list {my_list}")


# while continue_game:
#     print("=========================================")
#     print(f"====== {welcome_message} =======")
#     print("=========================================")

#     player_name = input("Please enter your name: ")
#     glasses_print = "[]"
#     glasses = [glasses_print] * 4
#     print(f"Hello {player_name}, please choose which glass you are thinking of a number between 1 and 10")

#     guess = input("Please guess a number or type 'exit' to quit: ")

#     match guess.lower():
#         case 'exit':
#             continue_game = False
#         case _ if int(guess) == ball_position:
#             print(f"You got it! The Ball Position is on {ball_position} and You guessed {guess}")
#         case _:
#             print(f"You did not get it :( The Ball Position is on {ball_position} and You guessed {guess}")
    
#     print("=========================================")
