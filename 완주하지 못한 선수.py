# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    a = {}

    for i in completion:
        if i not in a.keys():
            a[i] = 1
        else:
            a[i] = a[i] + 1

    for j in participant:
        if j not in a.keys():
            return j
        else:
            a[j] = a[j] -1
            if a[j] == -1:
                return j


#다른답 -> counter객체는 서로 뺄 수 있다는것을 이용
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]