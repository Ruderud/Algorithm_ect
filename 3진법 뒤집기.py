# https://programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    answer = 0

    tri = []
    e = 0

    while 3**e < n:#a
        e+=1

    for i in range(e,-1,-1):#b
        tri.append(n//(3**i))
        n = n%(3**i)

    count=0
    if tri[0] == 0:#c
        del tri[0]

    for j in tri:#d
        answer+=j*(3**count)
        count+=1

    return answer

n = 27

print(solution(n))


# def solution(n):
#     tmp = ''
#     while n:                  ->위 답의 a와 b의 역할을 한번에 수행함. 처음부터 3으로 나눠가면서 3진수형태의 문자열을 역순으로 tmp에 저장했음.
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)      ->저장된 문자열 tmp가 사실 3진수 형태임을 알려주고, 이를 int()를 사용하여 10진수화 했음
#     return answer

print(int('1111',2)) #15출력. int()에는 이런기능도있음.