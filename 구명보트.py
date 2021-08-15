# https://programmers.co.kr/learn/courses/30/lessons/42885s
from collections import deque

def solution(people, limit):
    answer = 0

    people = deque(sorted(people))

    while people:
        light = people.popleft()

        while people and light + people[-1] > limit:
            if not people:
                return answer + 1
            people.pop()
            answer += 1

        if people:
            people.pop()
            answer += 1
        else:
            answer += 1

    return answer

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    #가벼운사람의 좌표(a), 무거운사람의 좌표(b)를 비교해가며 같이 탈수있다면 answer+=1, 이후 같이탈수없는사람만 남으면(a>=b) 남은사람은 혼자타야하는사람들
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
