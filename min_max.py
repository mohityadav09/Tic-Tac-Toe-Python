import tic_tac_toe as tt
import copy

a='X'
b='O'

def minmax(position, maximizingPlayer, depth=100000, alpha=-10000000, beta=1000000):
    game_over = tt.isGameOver(position)
    if depth == 0 and not game_over[0]:
        res = tt.success_x(position) - tt.success_o(position)
        return res
    if game_over[0]:
        if game_over[1] == 'AI':
            return 10000
        if game_over[1] == 'Human':
            return -10000
        if game_over[1] == 'Draw':
            return 0

    if maximizingPlayer:
        max_eval = -10000
        for row in range(3):
            for col in range(3):
                if position[row][col] == '-':
                    temp = copy.deepcopy(position)  # Create a deep copy
                    temp[row][col] = a
                    evaluation = minmax(temp, False, depth - 1, alpha, beta)
                    max_eval = max(max_eval, evaluation)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = 10000
        for row in range(3):
            for col in range(3):
                if position[row][col] == '-':
                    temp = copy.deepcopy(position)  # Create a deep copy
                    temp[row][col] = b
                    evaluation = minmax(temp, True, depth - 1, alpha, beta)
                    min_eval = min(min_eval, evaluation)
                    beta = min(beta, evaluation)  # Corrected: use min(beta, evaluation)
                    if beta <= alpha:
                        break
        return min_eval


#print(minmax(example,True,2))

def bestNextMove(example):
    best=-1000000000
    next_move = [['', '', ''], ['', '', ''], ['', '', '']]
    for row in range(3):
        for col in range(3):
            if example[row][col] == '-':
                x_=copy.deepcopy(example)
                x_[row][col]= a
                score = minmax(x_, False, 1)
                if score > best:
                    best = score
                    next_move = x_
    return next_move




tic_table = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

while not tt.isGameOver(tic_table)[0]:  # Continue playing until the game is over
    tt.display(tic_table)
    x = int(input('Input index of row of your move: '))
    y = int(input('Input index of col of your move: '))
    tic_table[x][y] = b
    if not tt.isGameOver(tic_table)[0]:  # Check if game is still ongoing after human move
        tic_table = bestNextMove(tic_table)
    else:
        break

tt.display(tic_table)

game_over, winner = tt.isGameOver(tic_table)
if winner == 'Draw':
    print("It's a draw!")
else:
    print(f"{winner} is the winner!")

"""example=[[b,a,'-'],['-','-','-'],[b,'-','-']]
x_o=bestNextMove(example)
tt.display(x_o) """

