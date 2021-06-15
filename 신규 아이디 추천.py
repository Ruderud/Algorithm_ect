#https://programmers.co.kr/learn/courses/30/lessons/72410

new_id = "abcdefghijklmn.p"

def solution(new_id):

    first_str = ''
    new_id = new_id.lower()             #1단계
    print('1단계', new_id)
    for first in new_id:                #2단계 진행
        if 97 <= ord(first) <= 122 or 48 <= ord(first) <= 57 or ord(first) in [45,46,95] :
            first_str+=first
        else:
            continue
    print('2단계', first_str)

    second_str = ''
    second_str += first_str[0]          #3단계
    for second in first_str[1:]:
        if second_str[-1] == '.' and second == '.':
            continue
        else:
            second_str += second
    print('3단계', second_str)

    if second_str[0] == '.': second_str = second_str[1:]          #4단계
    print('4.5단계', second_str)
    if second_str and second_str[-1] == '.': second_str = second_str[:-1]
    print('4단계', second_str)

    if not second_str: second_str += 'a'                #5단계
    print('5단계', second_str)

    if len(second_str) >= 16 : second_str = second_str[:15]      #6단계
    print('6단계', second_str)

    while len(second_str) < 3: second_str+=second_str[-1]       #7단계
    print('7단계', second_str)

    if second_str[0] == '.': second_str = second_str[1:]          #4단계 한번더!
    print('4.5단계', second_str)
    if second_str and second_str[-1] == '.': second_str = second_str[:-1]
    print('4단계', second_str)
    return second_str

print(solution(new_id))