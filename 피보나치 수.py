# https://programmers.co.kr/learn/courses/30/lessons/12945
import sys
sys.setrecursionlimit(10**7) #재귀제한을 늘림

def solution(n):
    answer = 0

    box=[0,1]

    def pibo(a):
        if len(box) > a:
            return box[a]
        else:
            box.append(pibo(a-2)+pibo(a-1))
            return box[a]

    answer = pibo(n)

    return answer%1234567

# 다른풀이: 문제의 조건인 1234567로 나눈 나머지 수만 이용해서 n번째까지의 피보나치 수열을 계산
def solution(n):
    f_list = [0,1]
    for i in range(2,n+1):
        f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
    return f_list[-1]