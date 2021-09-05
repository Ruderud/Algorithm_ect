# https://programmers.co.kr/learn/courses/30/lessons/77485

def rotate(array, query):
    ax, ay = query[0]-1, query[1]-1
    bx, by = query[2]-1, query[3]-1

    x,y = [ax+1, ay]
    save_val = array[ax+1][ay]
    min_num = save_val

    while x != ax or y != ay:
        print(x,y)

        if y == ay and x != bx:
            nx = x + 1
            ny = y
        elif x == bx and y != by:
            nx = x
            ny = y + 1
        elif y == by and x != ax:
            nx = x - 1
            ny = y
        elif x == ax:
            nx = x
            ny = y - 1

        array[x][y] = array[nx][ny]
        print(array[nx][ny])
        min_num = min(min_num, array[nx][ny])
        
        x = nx
        y = ny

    array[ax][ay] = save_val

    return array, min_num

def solution(rows, columns, queries):
    answer = []

    array = []
    num = 1
    for _ in range(rows):
        array.append([i for i in range(num,num+columns)])
        num += columns
    
    print(array)

    for query in queries:
        array, min_num = rotate(array, query)
        answer.append(min_num)
        print('+'*10)
        for i in array:
            print(i)

    return answer

rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))