# https://programmers.co.kr/learn/courses/30/lessons/70128 

def solution(a, b):
    answer = 0
    for i in range(len(a)): answer+=a[i]*b[i]
    return answer

def solution(a,b):
    return sum([x*y for x,y in zip(a,b)])

a = ['a','b']
b = [-1,0,1]
c = ['가','나']

for tuple in zip(a,b,c):
    print(tuple)     # "('a', -1, '가')
                    #  ('b', 0, '나')"가 출력된다. 
                    #즉, zip(a,b,c...**kwargs(n번째))은 n 가지의 iterables한것을 a[0], b[0], c[0]꼴로 index에 맟춰 일대응대응시켜서 튜플로 반환한다.