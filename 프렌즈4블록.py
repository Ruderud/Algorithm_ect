# https://programmers.co.kr/learn/courses/30/lessons/17679

def erase(m,n,board):
    target = []
    
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != '0' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                target.append((i,j))
                target.append((i,j+1))
                target.append((i+1,j))
                target.append((i+1,j+1))
    
    target_set = set(target)

    for i,j in target_set:
        board[i][j] = ''

    for y in range(n):
        vertical = ''
        for x in range(m-1,-1,-1):
            vertical+=board[x][y]
        vertical = vertical.ljust(m,'0')
        
        for x,rev_x in zip(range(m-1,-1,-1), range(m)):
            board[x][y] = vertical[rev_x]

    return board, len(target_set)


def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        board, erase_count = erase(m,n,board)

        if erase_count:
            answer+=erase_count
        else:
            break

    return answer

# m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"] #return 14
m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] #return 15
print(solution(m,n,board))