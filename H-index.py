# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if i <= citations[i]:
            answer = max(min(i+1, citations[i]), answer)

    # print(citations)
    return answer

#직관적으로 풀었음... 내림순으로 정렬해서 내려갈때, 내려간 논문수와 인용수중 작은수를 갱신하면서 최대 h값을 반환하면된다
#git author 변환용 커밋