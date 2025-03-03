templqte = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
N = 5
buttons = N - 2 
button_start = 2
button_end = N - 1
special_buttons = [i for i in range(button_start, button_end + 1)]

def flip(state, index):
    #flip current state also prev and next state if state is 0
    if state[index] == 1:
        state[index] == 0 
        state[index - 1] = 1 if state[index - 1] == 0 else 0
        state[index + 1] = 1 if state[index - 1] == 0 else 0

for i in range(len(templqte)):
    print("")
    
flip(templqte, )
# print(f"flip {flip(templqte, N)}")
# print(f"flip {templqte}")
# flip(templqte, N)
# print(f"flip {templqte}")


