# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0

    numbers = list(numbers)
    per_list = []

    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            a = int("".join(j))
            if a not in per_list:
                per_list.append(a)

    print(per_list)

    for num in per_list:
        check = True
        if num == 0 or num == 1:
            continue

        for c in range(2,int(num**0.5)+1):
            if num%c == 0:
                check = False
        
        if check:
            answer+=1

    return answer

numbers = "011"
print(solution(numbers))


from itertools import permutations

def solution1(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))  #문자열 조합으로 만들 수 있는 숫자를 set에 할당한다(중복 자동제거)
        print(a)

    a -= set(range(0, 2)) #0,1을 제거

    #가장 큰수에 대한 2 ~ a**0.5 사이 정수 범위를 만들고, 범위내의 각각의 정수값을 1step으로하는 배수set을 만들어, 그 배수set에 해당하는 값을 a에서 제거한다
    for i in range(2, int(max(a) ** 0.5) + 1):
        print(set(range(i * 2, max(a) + 1, i)))
        a -= set(range(i * 2, max(a) + 1, i))
        print(a)
    return len(a)


numbers = "011"
print(solution1(numbers))