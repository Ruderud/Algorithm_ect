# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    def gcd(a,b):
        if b == 0 : return a
        return gcd(b, a%b)

    a = 1
    for b in arr:
        c = gcd(a,b)
        a = a * b // c

    return a

#다른답: gcd메서드를 아예 가져올 수도 있음. Math 라이브러리에도 있음
from fractions import gcd
def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer