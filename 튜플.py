# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    
    p = 1
    s_len = len(s)
    
    num_str = ['0','1','2','3','4','5','6','7','8','9']
    bigbox = []
    box = []
    number = ''
    while p < (s_len -1):
        if s[p] == '{':
            box = []
            p+=1
        
        elif s[p] in num_str:
            number += s[p]
            p+=1
            
        elif s[p] in num_str and s[p+1] == '}':
            number += s[p]
            box.append(int(number))
            number = ''
            p+=1
        
        elif s[p] == "}" and s[p+1] == ',': #숫자끝 집합끝
            box.append(int(number))
            number = ''
            p+=1
            
        elif s[p] == "}" and s[p+1] == '}': #맨끝
            box.append(int(number))
            number = ''
            bigbox.append(box)
            box = []
            p+=1
        
        elif s[p] == "," and s[p+1] == "{":
            bigbox.append(box)
            p+=1
        
        elif s[p] == "," and s[p+1] in num_str: #숫자끝
            box.append(int(number))
            number = ''
            p+=1

    bigbox.sort(key = len)
    
    for num_set in bigbox:
        for num in num_set:
            if num not in answer:
                answer.append(num)

    
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

#그냥 s[2:-2]구간을 },{ 기준으로 split했으면 저런짓 안했다...