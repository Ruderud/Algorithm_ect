# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0

    priorities = [(priorities[i],i) for i in range(len(priorities)) ]
    q = deque(priorities)

    while q:
        printing = q.popleft()

        if q:
            for check in q:
                if check[0] > printing[0]:
                    q.append(printing)
                    break

            if q[-1] == printing:
                continue
            elif printing[1] == location:
                return answer + 1
            else:
                answer += 1
        else:
            return answer + 1


    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))

#다른답
def solution(priorities, location):
    #enumerate: list같은 iterable요소([val1, val2, ...])를 받아와서, [ (0, val1), (1, val2) ... (index, value) ] 로 반환
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0) #맨앞 요소를 가져온다는 의미... 이는 진짜 queue가 아닌, stack을 유사 queue처럼 사용하기에 속도는 느리다
        #any: iterable elements중 하나라도 조건에 부합시 true반환 
        #조건에 부합시 큐에 다시 넣고
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        #그렇지 않을시지금까지 출력한 것 갯수 +1, 이때 출력물이 target이라면 답을 반환
        else:
            answer += 1
            if cur[0] == location:
                return answer