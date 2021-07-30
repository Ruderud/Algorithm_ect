# https://programmers.co.kr/learn/courses/30/lessons/42746

'''
def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        if 0<= numbers[i] <10:
            numbers[i] = '0.' + str(numbers[i]) + '9'
        elif 10<= numbers[i] <100:
            numbers[i] = '0.' + str(numbers[i]) + '0002'
        elif 100<= numbers[i] <1000:
            numbers[i] = '0.' + str(numbers[i]) + '0001'
        else:
            numbers[i] = '0.' + str(numbers[i]) + '0000'
        
    numbers.sort(reverse=True)

    print(numbers)

    for i in range(len(numbers)):
        if numbers[i][6] == '3':
            answer += numbers[i][2]
        elif numbers[i][6] == '2':
            answer += numbers[i][2:4]
        elif numbers[i][6] == '1':
            answer += numbers[i][2:5]
        else:
            answer += numbers[i][2:6]

    if list(answer).count('0') == len(answer):
        return '0'

    return answer

def solution(numbers):
    if len(numbers)==1: return str(numbers[0])
    numbers = list(map(str, numbers)) # O(n)
    numbers = [(num, len(num)) for num in numbers] # O(n)
    new_nums = list()
    ths = 0 # 1000?
    zero = 0 # num of zeros
    for num, length in numbers: # O(n)
        if num == '0':
            zero += 1
            continue
        if length==1:
            new_nums.append((num*3, length))
        elif length==2:
            new_nums.append((num+num[0], length))
        elif length==4:
            ths += 1
        else:
            new_nums.append((num, length))
    #print(new_nums)
    new_nums.sort(key=lambda x: (x[0][0], x[0][1], x[0][2]), reverse=True) # O(nlogn)

    ans = str()
    for num, length in new_nums:
        ans += num[:length] # O(n)

    return str(int(ans + '1000'*ths + '0'*zero))

from itertools import permutations
def check(numbers):

    a = 0
    for i in list(permutations(list(map(str, numbers)),len(numbers))):
        a = max(a, int(''.join(i)))
    
    return a
'''

# numbers = [0,1,103]
# numbers1 = [0,1,103]
# print(solution(numbers))
# print(check(numbers1))


#해답
def solution(numbers):
    numbers = list(map(str, numbers)) #요소들을 int -> str화
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# numbers가 최대 3자리까지 이므로, 이를 이용하여 문자열 요소를 3배로 늘인것끼리 비교하여 더 큰것을 앞으로 두게끔 정렬함

#해답2
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers] #정수항목들을 문자열로 바꿈
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    #cmp_to_key는 2개의 인자를 가져와서, 비교하여 작으면 음수, 같으면 0, 크면 양수를 반환함
    answer = str(int(''.join(n)))
    return answer

'''
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result) // [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

이와같이 정렬대상을 두개씩 가져와서 검사하는데, 이떄 1 0 -1값을 이용하여 계속 정렬을 수행한다.

'''

numbers = [0,1,103]
numbers1 = [0,1,103]
print(solution(numbers))