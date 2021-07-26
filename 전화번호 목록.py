# https://programmers.co.kr/learn/courses/30/lessons/42577#
#Dictonary가 해쉬방법으로 탐색한다는것을 이용한다

def solution(phone_book):
    answer = True
    
    head_num = {}
    for num in phone_book:
        head_num[num] = 1

    for i in phone_book:
        len_i = len(i)
        check = True
        for j in range(len_i+1):
            if head_num.get(i[0:j]) == 1 and i[0:j] != i:
                answer = False
                check = False
                break
        if not check :
            break
    
    return answer

#다른사람답
def solution(phoneBook):
    #숫자를 오름차순 정렬하면 현재 검사하는 접두사번호보다 낮은숫자로 시작하는것이 없다는것을 이용
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        # str.startswith(prefix[, start[, end]]) => 문자열이 지정되어있는값 (p1)으로 시작하면 true, 아니면 false를 반환한다. 
        # start,end는 검사하는 위치를 지정할때 추가적으로 적용한다
        if p2.startswith(p1):
            return False
    return True