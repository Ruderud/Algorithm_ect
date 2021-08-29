# https://programmers.co.kr/learn/courses/30/lessons/17687

def translate(n, num):
    #16진법까지
    numcode = "0123456789ABCDEF"
    result = ""

    while num != 0:
        result += numcode[num % n]
        num = num // n

    return list(reversed(list(result)))

def solution(n, t, m, p):
    answer = ''
    
    sol_list = ['0']

    num = 0
    while len(sol_list) < t * m:
        sol_list += translate(n, num)
        num += 1

    print(sol_list)

    for i in range(len(sol_list)):
        if i % m == p - 1:
            answer += sol_list[i]
        if len(answer) == t:
            break
    
    return answer


print(solution(16,16,2,1))
