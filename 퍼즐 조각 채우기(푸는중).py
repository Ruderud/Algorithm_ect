# https://programmers.co.kr/learn/courses/30/lessons/84021


def find_pieces(table):
    pieces = []

    n = len(table)

    #동남서북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    

    for x in range(n):
        for y in range(n):

            if table[x][y] == 1:
                for d in range(3):
                    nx = x + dx[d]
                    ny = y + dy[d]
            



    return pieces

def solution(game_board, table):
    answer = -1
    
    
    pieces = find_pieces(table) #table의 조각들을 직사각형 꼴로 각각 잘라냄
    print(pieces)
    '''
    for piece in pieces:
        spined = []
        spin(piece) #90도씩 회전한 피스 총 4가지를 반환
        
        for spined_piece in spined: #4가지 피스중 하나씩 가져와서 game_board에 끼워보고 맞으면 
            correct = False
            for x in range(n-sx): #회전한 사각형의 세로,가로길이를 제외한 만큼만 좌표를 움직임
                if correct:
                    break
                for y in range(n-sy):
                    #그자리에 넣어보고 들어간다면, 블록의 1 주위에 인접한 0이 있는지 확인후
                    #있다면 continue, 없다면 correct =true하고 블록의 1갯수만큼 result에 추가
                    if correct:
                    break
    '''
    
    
    return answer

game_board = [
    [1,1,0,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
    ]

table = [
    [1,0,0,1,1,0],
    [1,0,1,0,1,0],
    [0,1,1,0,1,1],
    [0,0,1,0,0,0],
    [1,1,0,1,1,0],
    [0,1,0,0,0,0]
    ]

print(solution(game_board, table))