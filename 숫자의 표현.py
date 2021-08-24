
def solution(n):
    answer = 0
    a,b = 1, 1
    while a <= n:
        if (a+b) * (b-a+1) == 2 * n:
            answer += 1
            a += 1
            b = a
        else:
            b += 1
            if (a+b) * (b-a+1) > 2*n:
                a+=1
                b=a

    return answer


#다른답: 연속된 자연수로 n을 표현하는 방법의 가짓수는, n보다 작은 홀수로 n을 나누었을때 나머지가 0이되는 홀수의 갯수 (등차수열공식 응용)
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])