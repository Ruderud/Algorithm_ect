# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque

def solution(progresses, speeds):
    answer = []

    pro_q = deque(progresses)
    sp_q = deque(speeds)

    while pro_q:
        before_dev_count = len(pro_q)

        complete = 0
        # print('일과시작')
        for i in range(before_dev_count):
            pjt, dev = pro_q.popleft(), sp_q.popleft()
            pjt += dev
            pro_q.append(pjt)
            sp_q.append(dev)

        while pro_q and pro_q[0] >= 100:
            a,b= pro_q.popleft(), sp_q.popleft()
            # print('완성')
            complete += 1

        if complete:
            answer.append(complete)

    return answer

#다른답
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    #개발중인것이 있을때,
    while len(progresses)> 0:
        #맨앞 기능이 완성되었다면 개발중인 리스트에서 제거하고 완료카운트+1
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        #그렇지 않다먄 개발완료까지 필요한 시간을 1추가함, 이때 완료된 기능들이 있다면 이것들을 정답에 추가
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
