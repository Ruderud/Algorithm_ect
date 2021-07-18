# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []

    used = []
    person = 0
    cycle = 0

    p = 0
    while p < len(words):
        print(used, person, cycle)
        if not used:
            used.append(words[p])
            person+=1
            p+=1

        else:
            if used[-1][-1] == words[p][0] and words[p] not in used:
                used.append(words[p])
                person+=1
                p+=1

                if person == n:
                    cycle+=1
                    person=0

            else:
                answer.append(person+1)
                answer.append(cycle+1)
                break

    if not answer:
        answer = [0,0]

    return answer

#다른사람 답변
#가독성 떨어지는 코드지만, 현재의 pointer값을 사람들의 수로 나눠서 나온 몫과 나머지로 사이클, 몇번째 사람인지 식별할 수 있는것은 좋음
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]