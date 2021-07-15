# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
from copy import deepcopy

dx = [0,1,0,-1]
dy = [1,0,-1,0]
rep2=[]

def bfs(maps,n,m,x,y,count,end):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                print('출발좌표: (',x,',',y,')')
                # maps_cp = deepcopy(maps)
                # maps_cp[nx][ny] = 2
                maps[nx][ny] = 2
                for line in maps:
                    print(line)
                x,y = nx,ny
                count+=1

                print('도착좌표: (',x,',',y,')')
                print('='*50)

                if x == n-1 and y == m-1:
                    # for line in maps_cp:
                    for line in maps:
                        print(line)
                    print("도착")
                    print('이동한 횟수:',count)
                    print('-'*50)
                    rep2.append(count)
                    end = True
                
                    # bfs(maps_cp,n,m,x,y,count)
                if not end:
                    bfs(maps,n,m,x,y,count,end)
                
def solution(maps):
    answer = []
    n,m = len(maps), len(maps[0])
    x,y = 0,0
    maps[x][y] = 2
    count=1
    
    bfs(maps,n,m,x,y,count,False)

    if not rep2:
        return -1
    else:
        return min(rep2)

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# print(solution(maps))


#해답
from collections import deque

def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])  #x,y,cost꼴로 deque에 입력

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if 0<=nx<x_h and 0<=ny<y_h: #다음칸이 범위내에있고
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:   #그 칸이 아직가지않은곳(1)이거나, 현재 cost+1이 그 칸에 입력되어있는 필요 cost값보다 큰경우(개선가능여지가 있는 경우)
                    maps[ny][nx] = d + 1    #해당칸으로 움직이고, 그칸의 숫자에 cost값을 새겨넣는다
                    if nx == x_h - 1 and ny == y_h - 1:     #그리고 최종목적지에 도달했다면 지금까지의 cost+1의 값을 반환한다
                        return d + 1
                    # for line in maps:
                    #     print(line)
                    # print('='*50)
                    queue.append((nx, ny, d + 1))           #(최종목적지 도달x시) 도착한칸의 좌표와, 그 칸까지의 cost를 다시 deque에 넣는다

    return -1   #deque에있는 행동가능한 좌표를 모두 검사했는데도 목적지에 도달하지 못하면 -1을 반환

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))