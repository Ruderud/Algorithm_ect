#https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/


def twoEggDrop(n):

    def dp(m, eggs):
        if eggs == 1 or m <= 1: return m #알이 하나남았거나, 탐색할 층이 1칸 이하라면 입력된 칸 m을 반환

        res = float('inf') #초기 res값을 무한으로 초기화

        for f in range(1, m + 1):                       #알이 깨지는 기준이 되는 층 f를 1~m+1범위에서 순차적으로 검사
            res = min(res,                              #재귀로인해 저장된 res값과
                      1 + max(                          #1과 2의값중 큰값 +1과 비교하여 더 작은 값을 저장

                                dp(f - 1, eggs - 1),    #1. 알이 1개일떄 -> f까지의 층수-1 (원래 문제의 범위)를 범위를 반환
                                dp(m - f, eggs))        #2. 알이 2개일때 -> 입력한 최대층에서 깨지는 기준층 f까지의 거리를 반환
                            )
        return res 
        
    return dp(n, 2)

print(twoEggDrop(7))