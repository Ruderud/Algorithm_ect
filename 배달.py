# https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    answer = 0

    INF = 1e9
    graph = [[INF] * N for _ in range(N)]

    for start, end, cost in road:
        graph[start-1][end-1] = min(cost, graph[start-1][end-1])
        graph[end-1][start-1] = graph[start-1][end-1]

    for k in range(N):
        for x in range(N):
            for y in range(N):
                if x != y:
                    graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])
                else:
                    graph[x][y] = 0

    for node in graph[0]:
        if node <= K:
            answer+=1

    return answer

# N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4

print(solution(N, road, K))




#다른답: DFS적으로 해결

import sys
def solution1(N, road, K):
    visited, D, r = [False]*(N+1), [sys.maxsize]*(N+1), [[(None, None)]] + [[] for _ in range(N)]
    #sys.maxsize = 배정가능한 최대값

    for e in road:
        r[e[0]].append((e[1],e[2]))
        r[e[1]].append((e[0],e[2]))

    print(r)

    D[1] = 0
    for _ in range(1,N+1): 
        min_ = sys.maxsize
        for i in range(1,N+1): 
            if not visited[i] and D[i] < min_:
                min_ = D[i]
                m = i
        visited[m] = True
        for w, wt in r[m]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt

    return len([d for d in D if d <= K])

N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution1(N, road, K))