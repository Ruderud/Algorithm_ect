# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = []
    answer = filter(lambda x : x not in list(range(0,10)), numbers)
    
    return dict(answer)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))