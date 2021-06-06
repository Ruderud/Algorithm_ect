

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    max_deep = len(board)
    bucket = []

    for move in moves:
        depth = 0

        while depth < max_deep:
            pick = board[depth][move-1]
            board[depth][move-1] = 0

            if pick != 0:
                bucket.append(pick)
                break

            depth+=1

        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            del bucket[-2:]
            answer+=2
    
    return answer

print(solution(board, moves))