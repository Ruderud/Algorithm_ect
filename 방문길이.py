# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):

    move = { 'U':(1,0), 'D':(-1,0), 'L':(0,-1), 'R':(0,1) }
    x,y = 0,0
    road = set()

    for i in list(dirs):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.add(tuple(sorted([(x,y), (nx,ny)])))
            x = nx
            y = ny

    return len(road)