# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    zero = 0
    cycle = 0
    
    while s != '1':

        one = 0
        for i in list(s):
            if i == '1':
                one += 1
            else:
                zero += 1
            
            s = bin(one)[2:]
        cycle += 1
    
    answer = [cycle, zero]
    
    return answer