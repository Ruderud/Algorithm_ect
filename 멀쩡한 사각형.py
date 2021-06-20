# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3

# y = -(H/W)x + h 의 선형방정식을 세우고, x=1,2,3...w-1순으로 대입해서 y값의 정수부분값을 다 더하고, 그값을 두배하면 원하는 결과
# +개선안 -> 1,3,5,7,9로 하나씩 건너가며 계산을하는데, h - (x*h/w)의 정수값이 바뀌게되면 점프한값을 별도로 계산하여 추가한다.

w,h = 11,13

# def mini_solution(w,h):      #protoType
#     answer=0

#     for x in range(1,w):
#         answer+=((h*w)-(x*h)) // w

#     return answer

# from math import gcd

# def solution(w,h):
#     n = gcd(w,h)

#     if n == 1:                          #최대공약수가 1일때 = w,h중 하나라도 소수가있어서 반복구간이 없을때
#         return mini_solution(w,h) *2

#     else:
#         mini_h = int(h/n)
#         mini_w = int(w/n)
#         a = mini_solution(mini_w,mini_h)
#         sliced = (mini_w * mini_h) - (a*2)
#         return (w*h) - (n*sliced)
        
# print(solution(w,h))


#해답
from math import gcd
def solution(w,h):
    return (w*h) -w -h +gcd(w,h)    #전체넓이에서 가로길이만큼 제거, 세로길이만큼제거하고, 중복으로 제거된것중 최소공배수에 해당하는 칸은 다시 더해줘야함

print(solution(w,h))