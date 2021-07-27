from bisect import bisect_left, bisect_right
from collections import deque


def solution(n, times):
    
    answer = 0

    #모든사람이 다먹는상황 ~ 가장 느려터진사람이 혼자 다쳐먹는 말도 안되는 상황
    min_t, max_t = n // len(times), n * max(times)

    while min_t < max_t:
        #말도안되는 양 극단에서의 중간시점
        mid = (min_t + max_t) // 2

        people = 0

        #중간시간에 대해 각각의 시간으로 나눠서 처리하는 사람수를 구해봄
        for time in times:
            people += mid//time

        #처리인구수가 n보다 많으면 줄일수있고
        if people >= n:
            max_t = mid
        #부족하면 더 늘려야함
        elif people < n:
            min_t = mid + 1
    
        print(min_t, max_t)
    
    #끝까지 조여서 좌우가 같아지면 끝
    answer = min_t

    return answer

n, times = 100, list(range(1,100))
print("결과값: ",solution(n, times))



# a = deque([[10,4],[14,2],[15,3],[18,1]])

# print(bisect_left(a, [11,5]))

