# https://programmers.co.kr/learn/courses/30/lessons/12899#

def solution(n):
    answer = ''
    
    region124 = []
    
    p = 1
    while True:
        a = n%(3**p)
        b = n//(3**p)
        
        if a == 0:
            a = 4
            b -= 1
        
        if not b:
            region124.append(a)
            break
        
        else:
            region124.append(a)
            n = b
    
    region124.reverse()

    for i in region124:
        answer+=str(i)

    return answer


#다른사람 풀이
def change124(n):
    if n<=3:
        return '124'[n-1] #문자열에 바로 index를 쓸수있다!
    else:
        q, r = divmod(n-1, 3)  #divmod(a,b)는 return (a//b), (a%b)를 반환하는 나누기 함수이다
        return change124(q) + '124'[r]