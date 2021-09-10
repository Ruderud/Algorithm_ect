

def solution(number, k):
    
    erase = []
    number += "a"
    p = 0
    while k:
        print('qwe', erase)
        
        if number[p] < number[p+1]:
            erase.append(p)
            bp = p - 1
            k -= 1
            if not k:
                break
            while bp >= 0 and number[bp] < number[p+1]:
                print('asd', erase)

                if bp not in erase:
                    erase.append(bp)
                    bp -= 1
                    k -= 1
                else:
                    break

                if not k:
                    break
        p += 1
        
    print('end', erase)

    erase.sort()
    number = number[:-1]

    answer = ""

    for i in range(len(number)):
        if i not in erase:
            answer += number[i]
        
    return answer

# print(solution("1231234",3))

#다른답
def solution1(number, k):
    stack = [number[0]]
    for num in number[1:]:
        print(stack)
        #스택에 값이 있고, 스텍의 마지막값이 검사하는 number의 num보다 작고, 제거해야할 숫자 갯수가 남아있을때 => 스텍의 숫자를 제거하고 k를 1줄인다
        #그렇지 않은경우는 그냥 남긴다
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        #다음 숫자를 스텍에 넣는다
        stack.append(num)
    
    #뒷숫자보다 작은 앞숫자를 전부 제거해도 더 제거해야야할 숫자가 남았다면, 뒤에서부터 남은 k만큼 제거
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

print(solution1("1231234",3))