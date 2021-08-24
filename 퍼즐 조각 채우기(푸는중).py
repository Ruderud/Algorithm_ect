# https://programmers.co.kr/learn/courses/30/lessons/84021

#게임보드를 3n * 3n으로 확장시킨후, (1,1)부터 (2n,2n) 까지 table을 0/90/180/270 도 순서로 대보는 작업수행

#90도회전
def rotate90d(table):
    n = len(table)
    new_table = [ [0] * n for _ in range(n) ]

    for i in range(n):
        for j in range(n):
            new_table[j][n-1-i] = table[i][j]
    
    return new_table



def solution(game_board, table):
    answer = -1
    
    n = len(game_board)
    wide_board = [ [0] * 3 * n for _ in range(3*n)]

    for i in range(n):
        for j in range(n):
            wide_board[i+n][j+n] += game_board[i][j]
            if i == 0 :
                wide_board[n-1][j+n] += 1
            if i == n-1 :
                wide_board[n+n][j+n] += 1
            if j == 0 :
                wide_board[i+n][j+n-1] += 1
            if j == n-1 :
                wide_board[i+n][n+n] += 1
            if table[i][j] == 1:
                table[i][j] += 1


    for z in wide_board:
        print(z)
    
    for i in table:
        print(i)

    for i in range(1,2*n):
        for j in range(1,2*n):
            
            check = True
            for x in range(n):
                for y in range(n):
                    wide_board[i+x][j+y] += table[x][y]
                    if wide_board[i+x][j+y] == 3:
                        check = False


                    
            if check:
                for xi in range(i, i+n):
                    for yj in range(i, i+n):
                        
                        if wide_board[xi][yj] == 2 and 0 in [wide_board[xi-1][yj],wide_board[xi+1][yj],wide_board[xi][yj-1],wide_board[xi][yj+1]]:


                            

            
            for x in range(n):
                for y in range(n):
                    wide_board[i+x][j+y] -= table[x][y]

    
    
    
    
    return answer

# game_board = [
#     [1,1,0,0,1,0],
#     [0,0,1,0,1,0],
#     [0,1,1,0,0,1],
#     [1,1,0,1,1,1],
#     [1,0,0,0,1,0],
#     [0,1,1,1,0,0]
#     ]

# table = [
#     [1,0,0,1,1,0],
#     [1,0,1,0,1,0],
#     [0,1,1,0,1,1],
#     [0,0,1,0,0,0],
#     [1,1,0,1,1,0],
#     [0,1,0,0,0,0]
#     ]

game_board = [[0,0,0],[1,1,0],[1,1,1]]
table = [[1,1,1],[1,0,0],[0,0,0]]

print(solution(game_board, table)) 