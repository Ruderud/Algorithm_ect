#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for start,end,order in commands :
        array_temp = sorted(array[start-1:end])
        answer.append(array_temp[order-1])
    return answer