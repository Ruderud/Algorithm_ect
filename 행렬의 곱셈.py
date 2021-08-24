# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    rotate_arr2 = [ [] for _ in range(len(arr2[0]))]
    
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            rotate_arr2[j].append(arr2[i][j])
    
    answer = [ [] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for l2 in rotate_arr2:
            result = 0
            for a,b in zip(arr1[i], l2):
                result += a * b
            answer[i].append(result)

    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))

#다른답
def solution1(A, B):
    #zip(*B)는 행 단위로 요소들을 가져오는 메서드
    for B_col in zip(*B):
        print(B_col)

    print(list(zip(*B)))


    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(solution1(arr1, arr2))