# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer=[ ['#'] * n for _ in range(n) ]

    for i in range(n):
        arr1[i] = ('0' * n) + bin(arr1[i])[2:]
        arr2[i] = ('0' * n) + bin(arr2[i])[2:]
    
    for x in range(n):
        pointer=-1
        for y in range(n-1,-1,-1):
            if arr1[x][pointer] == arr2[x][pointer] == '0':
                answer[x][y] = ' '

            pointer = pointer -1

    answer2 = []
    for line in answer:
        answer2.append(''.join(line))
    
    return answer2


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n,arr1,arr2))

#다른해답
def solution_d(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):      #zip을 이용해 arr1, arr2를 하나씩 가져와서 묶음
        a12 = str(bin(i|j)[2:])     #각각의 2진수 str을 구한후, 이떄 둘중하나라도 1이면, 둘다0이면 0을 반환 ex) 1001|11110 -> 11111, 1001|1 ->1001
        a12=a12.rjust(n,'0')        #rjust -> n길이의 문자열공간을 만들고, 그 공간에 대해 위의 2진수 문자열을 오른쪽정렬하여 입력하고 나머지 빈공간은 0으로 매운다
        a12=a12.replace('1','#')    
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution_d(n,arr1,arr2))
print(bin(30))