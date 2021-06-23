#https://programmers.co.kr/learn/courses/30/lessons/77884

def div_c(num):
    div=1
    count=0
    while div<=num:
        if num%div == 0:
            count+=1
        div+=1
    return count

def solution(left, right):
    answer = 0

    for i in range(left,right+1):
        if div_c(i)%2==0:
            answer+=i
        else:
            answer-=i

    return answer

print(solution(13,17))

# 제곱수는 약수의 갯수가 홀수이다... 반대로 제곱수가 아니면 약수의 갯수가 짝수! 이것을 이용하면 더 간단히도 가능
