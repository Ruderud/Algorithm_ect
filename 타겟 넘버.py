# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    result = 0
    p = 0
    n = len(numbers)
    box = []

    def dfs(result,p):
        if p == n:
            box.append(result)

        else:
            for i in [1,-1]:
                dfs(result+(numbers[p]*i), p+1)

    dfs(result, p)

    answer = box.count(target)

    return answer



#다른답
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer