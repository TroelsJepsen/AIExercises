import sys

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    isTerminal = True
    for pile in state:
        if ( pile != "Min" and pile != "Max" and pile > 2) :
            isTerminal = False



def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    utility = 1
    if (is_terminal(state) and state[0] == "Max"):
        utility = -1
    return utility


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    potential_moves =[]
    player = "Max"
    if state[0] == "Max":
        state[0] = "Min"
    else:
        state[0] = "Max"
    move_number = 0
    for pile in state:
        if pile != "Max" or pile != "Min" or pile != 1 or pile != 2:
            y = pile
            x = 0
            state.remove(pile)
            while 2*x < pile:
                move_number = move_number +1
                x = x+1
                y = x-1
                succesing_state = state.copy()
                new_succesing_state.extend([x,y])
                potential_moves.append((move_number, succesing_state))
    return potential_moves




    if state.count('X') == state.count('O'):
        character = 'X'
    else:
        character = 'O'
    move_number = 0
    potential_moves =[]
    for position in state:
        if position != 'X' or 'Y':
            succesing_state = state.copy()
            succesing_state[move_number] = character
            potential_moves.append((move_number, succesing_state))

    return potential_moves



def display(state):
    print("-----" + state)



def main():
    sys.setrecursionlimit(10000)
    stateOfGame = ["Max", 6] # 0th place represents the player whose turn it is. The remaining represent the number of stones in each pile

    while not is_terminal(stateOfGame):
        board[minmax_decision(stateOfGame)] = 'X'
        if not is_terminal(stateOfGame):
            display(stateOfGame)
            board[int(input('Your move? '))] = 'O'
    display(stateOfGame)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
