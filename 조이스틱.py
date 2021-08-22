# https://programmers.co.kr/learn/courses/30/lessons/42860
from collections import deque
def solution(name):

    n = len(name)
    name = list(name)
    array = deque([[name[i],deque([chr(i) for i in range(65,91)])] for i in range(n)])
    count = 0

    while False in [array[i][0] == array[i][1][0] for i in range(n)]:

        p = 0
        while array[0][0] != array[0][1][0]:
            array[0][1].rotate(1)
            p += 1
        count += min(p, 26-p)

        if not False in [array[i][0] == array[i][1][0] for i in range(n)]:
            break

        right = 0
        while array[0][0] == array[0][1][0]:
            array.rotate(-1)
            right += 1
        array.rotate(right)
        
        left = 0
        while array[0][0] == array[0][1][0]:
            array.rotate(1)
            left -= 1
        array.rotate(left)

        if abs(right) > abs(left):
            array.rotate(-left)
            count += abs(left)
        else:
            array.rotate(-right)
            count += abs(right)
    
    return count

print(solution("ABAAAAAAAAABB"))

#다른답
def solution1(name):
    #name의 알파벳을 형성하기 위해 위 또는 아래로 움직여야할 최소 횟수
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]       

    answer = 0
    where = 0

    while True:    
        answer += m[where]
        m[where] = 0

        #앞으로 움직여야할 횟수가 전부 0이되면 break
        if sum(m) == 0:
            break

        left, right = (1,1)

        #포인터가 오른쪽/왼쪽으로 각각 갈때의 움직임량을 계산하여 다음 이동목적지 설정
        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer
print(solution1("ABAAAAAAAAABB"))