# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    n = len(nums)/2
    species = len(set(nums))

    if n>=species:
        answer=species
    else:
        answer=n
    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))