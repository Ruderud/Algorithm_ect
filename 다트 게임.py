#https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):

    period = [[] for _ in range(3)]
    calculate = {'S':1, 'D':2, 'T':3, '*':2, '#':-1}

    count=0
    for i in dartResult:
        if i in ['S','D','T']:
            period[count].append(i)
            count+=1
        elif i in ['*','#']:
            period[count-1].append(i)
        else:
            period[count].append(i)
    
    for per in period:
        if per[-1] not in ['*','#']:
            per.append('x')

    for per in period:
        if len(per) == 4:
            per[0] = int(per[0]+per[1])
            del per[1]
        else:
            per[0] = int(per[0])

    scores = []
    for point, cal, bonus in period:
        if bonus == '*' and not scores:
            scores.append((point**calculate[cal])*calculate[bonus])
        elif bonus == '*' and scores:
            scores[-1] = scores[-1]*calculate[bonus]
            scores.append((point**calculate[cal])*calculate[bonus])
        elif bonus == '#':
            scores.append((point**calculate[cal])*calculate[bonus])
        else:
            scores.append(point**calculate[cal])
    print(period, scores)
    return sum(scores)

dartResult = '1D2S3T*'

print(solution(dartResult))


'''정규식을 안쓴 다른답안

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')                   #두자리를 먹는 10을 k로 바꿔서 표현
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


'''