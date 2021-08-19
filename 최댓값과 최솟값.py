# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    a = list(map(int, s.split(' ')))
    return str(min(a)) + ' ' + str(max(a))