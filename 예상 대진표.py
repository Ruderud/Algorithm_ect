# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0

    compare = sorted([a,b])
    low = compare[0]
    high = compare[1]
    
    while True:
        if low%2 == 1 and high%2 == 0 and low+1 == high:
            break
        
        if low%2 == 1:
            low = (low//2) + 1
        else:
            low = low//2
        
        if high%2 == 1:
            high = (high//2) + 1
        else:
            high = high//2
        
        answer+=1
    

    return answer+1


#다른답
def solution1(n,a,b):
    return ((a-1)^(b-1)).bit_length()

n,a,b = 8,3,7
print(solution1(n,a,b))

#bit_length()는 숫자를 2진수로써변환했을때 표현에 사용된 bit갯수를 반환하는 메서드이다.
# a-1 = 2 = 010(2)      처음 1을 빼는 이유는 서로 만나기위해 대전하는 횟수 1회를 포함시키기 위해서이다
# b-1 = 6 = 110(2)
# ^(XOR)연산=100(2) => bit_length() = 3 
