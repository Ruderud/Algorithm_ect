# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    cost = 0
    d.sort()
    for i in d:
        cost+=i
        answer+=1
        if cost>budget:
            return answer-1
        elif cost==budget:
            return answer
        else:
            continue
    return answer





d, budget = [], 10
print(solution(d,budget))