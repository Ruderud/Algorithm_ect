# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = []
    for a,b in list(combinations(numbers,2)): answer.append(a+b)
    return sorted(set(answer))

numbers = [2,1,3,4,1]

print(solution(numbers))

#set('iterable')는 iterable한 요소내부 elements중, 중복된 요소를 제거하는기능이다.