# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []

    for num in numbers:
        #짝수는 그냥 1더하면 된다
        if num % 2 == 0:
            answer.append(num + 1)

        else:
            #홀수는 2진화 했을때, 뒤에서 처음으로 만나는숫자 0과, 그 0뒤에있는 1을 스왑해주면 된다. (홀수이므로 무조건 0뒤에 1이 존재)
            fn = list('0' + bin(num)[2:])
            for i in range(-1, -len(fn)-1, -1):
                if fn[i] == '0':
                    fn[i] = '1'
                    fn[i+1] = '0'
                    break
            answer.append(int('0b' + ''.join(fn), 2))

    return answer

#다른답: +1큰 수에 대해 XOR 연산시, 최초로 0이나온자리까지 1이 연속으로 된 숫자만 출력된다
# ex) 110111 ^ 111000 => 001111 여기서 val값을 더한후  >> 2 연산시 111010이되고, 이제 가장 가까운 짝수화가 되었으므로 +1을 하면 111011이 된다
def solution1(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        print(val, '연산시작')
        print((val ^ (val+1)))
        print(((val ^ (val+1)) >> 2))
        print(((val ^ (val+1)) >> 2) +val +1)
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

print(solution1([2,7]))