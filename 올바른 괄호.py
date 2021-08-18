# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = 0

    n = len(s)

    for i in range(n):
        if s[i] == '(':
            answer += 1
        else:
            answer -= 1

        if answer < 0:
            break

    return True if answer == 0 else False