# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    
    p = 1
    y_div = []
    
    while p <= int(yellow**0.5):
        if yellow%p == 0:
            y_div.append((p,yellow//p))
        p+=1
    
    print(y_div)
    
    for y_x,y_y in y_div:
        if (2*y_x) + (2*y_y) + 4 == brown:
            answer = [y_y+2, y_x+2]
    
    return answer