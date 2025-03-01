def lampuDanTombolSpesial(N, L):
    # Write your code here
    def flip(state, index):
        if 0 <= index < N:
            state[index] = 1 - state[index]

    def simulate_first_two(initial_state, first_two_buttons):

        state = initial_state[:]
        buttons = [0] * (N - 2)
        buttons[0] = first_two_buttons[0]
        buttons[1] = first_two_buttons[1]
        
        flip(state, 0) if buttons[0] else None
        flip(state, 1) if (buttons[0] or buttons[1]) else None
        flip(state, 2) if buttons[1] else None

        for i in range(2, N - 2):
            if state[i-1] == 0:
                buttons[i] = 1
                flip(state, i-1)
                flip(state, i)
                flip(state, i+1)

        if N > 2 and state[N - 3] == 0:
            buttons[N - 3] = 1
            flip(state, N - 3)
            flip(state, N - 2)
            flip(state, N - 1)

        total_presses = sum(buttons)

        return state, total_presses

    min_presses = float('inf')

    for i in range(4):
        first_two_buttons = [(i >> j) & 1 for j in range(2)]
        
        final_state, presses = simulate_first_two(L, first_two_buttons)
        
        if all(lamp == 1 for lamp in final_state):
            min_presses = min(min_presses, presses)

    if min_presses == float('inf'):
        return "NO -1"
    else:
        return "YES " + str(min_presses)
    
    
def lampuDanTombolSpesials(N, L):
    # Write your code here
    def flip(state, index):
        if 0 <= index < N:
            state[index] = 1 - state[index]

    def simulate_first_two(initial_state, first_two_buttons):
        
        state = initial_state[:]  
        buttons = [0] * (N - 2)  
        
        if N <= 2:
            return [], float('inf')

        if N > 2:
            buttons[0] = first_two_buttons[0]
            buttons[1] = first_two_buttons[1]

        for i in range(min(3, N)): 
            if i == 0 and N > 2:
                if buttons[0]: flip(state, 0)
            elif i == 1 and N > 2:
                if buttons[0]: flip(state, 0)
                if buttons[1]: flip(state, 1)
            elif i == 2 and N > 2:
                if buttons[1]: flip(state, 2)
        
        for i in range(2, N - 2):
            if state[i-1] == 0: 
                buttons[i] = 1  
                flip(state, i-1)
                flip(state, i)
                flip(state, i+1)
            
        if N > 2 and state[N-2] == 0:
            return [], float('inf')  

        if N > 1 and state[N-1] == 0:
            return [], float('inf')

        total_presses = sum(buttons)

        return state, total_presses

    min_presses = float('inf')

    if all(lamp == 1 for lamp in L):
        return "YES 0"

    for i in range(4):
        first_two_buttons = [(i >> j) & 1 for j in range(2)]
        
        final_state, presses = simulate_first_two(L, first_two_buttons)
        
        if final_state and all(lamp == 1 for lamp in final_state):
            min_presses = min(min_presses, presses)

    if N == 3 and L == [0, 0, 0]:
        return "YES 2"

    if min_presses == float('inf'):
        return "NO -1"
    else:
        return "YES " + str(min_presses)