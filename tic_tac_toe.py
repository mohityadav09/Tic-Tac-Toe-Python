a='X'
b='O'
v=[['-','-','-'],['-','-','-'],['-','-','-']]
def display(v):
    for list in v:
        x=''
        for num in list:
            x+=num
            x+='  '
        print(x)
def success_x(v):
    a_eval=0
    for list in v:
        count_b=0
        for i in v:
            if i==b:
                count_b+=1
    if count_b == 0:
        a_eval+=1

    for col in range(3):
        count_b=0
        for row in range(3):
            if v[row][col]==b:
                count_b+=1
        if count_b == 0:
            a_eval+=1

    if (v[0][0]!=b and v[1][1]!=b) and v[2][2]!=b:
        a_eval+=1

    if (v[0][2]!=b and v[1][1]!=b) and v[2][0]!=b:
        a_eval+=1

    return a_eval

def success_o(v):
    b_eval=0

    for list in v:
        count_a = 0
        for i in list:
            if i==a:
                count_a+=1
        if count_a == 0:

            b_eval+=1

    for col in range(3):
        count_a = 0
        for row in range(3):
            if v[row][col]==a:
                count_a+=1
        if count_a == 0:
            b_eval+=1



    if (v[0][0]!=a and v[1][1]!=a) and v[2][2]!=a:
        b_eval+=1


    if (v[0][2]!=a and v[1][1]!=a) and v[2][0]!=a:
        b_eval+=1


    return b_eval









def isGameOver(board):
    # Check rows, columns, and diagonals for a winning combination
    result=[]
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != '-':
            if board[i][0] == a:
                result.append(True)
                result.append('AI')
                return result
            else:
                result.append(True)
                result.append('Human')
                return result
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != '-':
            if board[0][i] == a:
                result.append(True)
                result.append('AI')
                return result
            else:
                result.append(True)
                result.append('Human')
                return result
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        if board[0][0] == a:
            result.append(True)
            result.append('AI')
            return result
        else:
            result.append(True)
            result.append('Human')
            return result
    if board[0][2] == board[1][1] == board[2][0] != '-':
        if board[0][2] == a:
            result.append(True)
            result.append('AI')
            return result
        else:
            result.append(True)
            result.append('Human')
            return result

    # Check if the board is full (tie)
    for row in board:
        for cell in row:
            if cell == '-':
                result.append(False)
                return result  # Game is not over yet
    result.append(True)
    result.append('Draw')
    return result  # Board is full but no winner, game is a tie


def minmax(position,maximizingPlayer,depth=2,alpha=-10000,beta=10000):
    game_over = isGameOver(position)
    if depth == 0:
        res = success_x(position) - success_x(position)
        return res
    if game_over[0]:

        if game_over[1] == 'AI' and  maximizingPlayer:
            return 10000
        if game_over[1] == 'Human' and maximizingPlayer==False:
            return -10000
        if game_over[1] == 'Draw':
            return 0


    if maximizingPlayer:
        max_eval = -10000
        for row in range(3):
            for col in range(3):
                if position[row][col] !='-':
                    temp=position
                    temp[row][col]=a
                    evaluation  = minmax(temp,False,depth-1,alpha,beta)
                    max_eval =  max(max_eval,evaluation)
                    alpha = max(alpha,evaluation)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval =10000
        for row in range(3):
            for col in range(3):
                if position[row][col] !='-':
                    temp=position
                    temp[row][col]=b
                    evaluation  = minmax(temp,True,depth-1,alpha,beta)
                    min_eval =  min(min_eval,evaluation)
                    beta = min(alpha,evaluation)
                    if beta <= alpha:
                        break
        return min_eval























