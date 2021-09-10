# https://programmers.co.kr/learn/courses/30/lessons/85002

def solution(weights, head2head):

    n = len(weights)
    boxers = [[i+1, weights[i]] for i in range(n)]

    for i in range(n):
        heavyWins = 0
        wins = 0
        fights = 0

        for j in range(n):
            if head2head[i][j] != "N":
                fights += 1
                if head2head[i][j] == "W":
                    wins += 1
                    if weights[i] < weights[j]:
                        heavyWins += 1

        if fights:
            boxers[i].append(wins/fights)
        else:
            boxers[i].append(0)
        boxers[i].append(heavyWins)

    print(boxers)
    boxers.sort(key = lambda x: (-x[2], -x[3], -x[1], x[0]))

    return [boxer[0] for boxer in boxers]

weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]
print(solution(weights, head2head))


#다른답: 데전결과를 담는 순서를 적절하게 조절해서, 역순정렬시 한번에 결과를 얻을 수 있도록함
def solution(weights, head2head):
    result = []
    l = len(weights)
    # 한 번에 정렬해서 풀어봅시다!
    ans = [[0 for _ in range(4)] for _ in range(l)] # 승률, 무거운복서 이긴횟수, 자기 몸무게, 번호(음수로)
    for i in range(l):
        ans[i][2] = weights[i]
        ans[i][3] = -(i+1)
        cnt = 0 # 판수
        for j in range(l):
            if head2head[i][j] == 'W':
                ans[i][0] += 1 # 일단 이김
                cnt += 1
                if weights[i] < weights[j]:
                    ans[i][1] += 1 # 무거운 복서 이김
            elif head2head[i][j] == 'L':
                cnt += 1 # 판수만 늘려준다
        if cnt == 0:
            ans[i][0] = 0
        else:
            ans[i][0] /= cnt
    ans.sort(reverse=True) # 역순으로 정렬하면 모든 조건이 한 번에 정렬된다

    for i in range(l):
        result.append(-ans[i][3])
    return result
