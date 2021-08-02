def solution(n, lost, reserve):
    answer = 0

    real_lost = []
    real_reserve = []

    for a in lost:
        if a not in reserve:
            real_lost.append(a)
    
    for b in reserve:
        if b not in reserve:
            real_reserve.append(b)


    print(real_lost,real_reserve)

    lost = real_lost
    reserve = real_reserve

    students = [9]
    for i in range(1,n+1):
        if i in lost:
            students.append(0)
        elif i in reserve:
            students.append(2)
        else:
            students.append(1)

    students.append(9)
    print(students)
    
    #좌우중 한명만 잃어버린애일때 운동복을 준다
    for j in reserve:
        if students[j-1] == 0 and students[j+1] != 0:
            students[j-1] += 1
            students[j] -= 1
            del reserve[reserve.index(j)]
        elif students[j-1] != 0 and students[j+1] == 0:
            students[j] -= 1
            students[j+1] += 1
            del reserve[reserve.index(j)]
    
    print(students)
    print(reserve)
    
    for k in reserve:
        if students[k-1] == 0:
            students[k-1] += 1
            students[k] -= 1
        elif students[k+1] == 0:
            students[k] -= 1
            students[k+1] += 1
            
    print(students)        
    
    for i in range(1,n+1):
        if students[i] != 0:
            answer += 1
    
    return answer

n = 3
lost = [1,2,3]
reserve = [1,2,3]
print(solution(n,lost,reserve))


def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer