# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def solution(s):
    answer = 0
    
    n = len(s)
    sq = deque(list(s))
    
    for _ in range(n):
        sqs = "".join(sq)
        print(sqs)

        sqs_len = n
        while sqs:
            sqs = sqs.replace("()", "")
            sqs = sqs.replace("{}", "")
            sqs = sqs.replace("[]", "")

            if len(sqs) == sqs_len:
                break

            sqs_len = len(sqs)
        
        if not sqs: answer += 1

        sq.rotate(-1)
            
    
    return answer

s = "}]()[{" 
print(solution(s))
