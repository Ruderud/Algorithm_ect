# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][a] for a in range(4) if a != j])

    return max(land[-1])

#TCT의 DP 금광문제와 비슷한 맥락! n+1번쨰 행의 점수들은 이전의 자신의 인덱스를 제외한 값중 큰값을 더한값임을 이용, 마지막행의 최대값을 구하면된다