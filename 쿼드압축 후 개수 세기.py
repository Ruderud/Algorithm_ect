# https://programmers.co.kr/learn/courses/30/lessons/68936

from collections import deque

def solution(arr):
    answer = [0,0]
    n = len(arr)
    sites = deque([[(0,0), (n,n)]])
    
    while sites:
        a, b = sites.popleft()
        count = 0
        for x in range(a[0], b[0]):
            for y in range(a[1], b[1]):
                if arr[x][y] == 1:
                    count += 1

        if count == 0:
            answer[0] += 1
        elif count == (b[0]-a[0]) ** 2:
            answer[1] += 1
        else:
            sites.append([(a[0],a[1]), ((b[0]+a[0])//2, (b[1]+a[1])//2)])
            sites.append([(a[0], ((b[1]+a[1])//2) ), ((b[0]+a[0])//2, b[1])])
            sites.append([(((a[0]+b[0])//2) , a[1]), (b[0] ,(b[1]+a[1])//2)])
            sites.append([(((b[0]+a[0])//2) , ((b[1]+a[1])//2) ), (b[0] ,b[1])])

    return answer

arr = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]]
print(solution(arr))