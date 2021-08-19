# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0

    while n:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1

    return ans

#다른답: 2로 나누면서 홀수일때 1을 빼주는 횟수 = 2진법 변환후, 1의 갯수
def solution(n):
    return bin(n).count('1')
