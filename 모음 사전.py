# https://programmers.co.kr/learn/courses/30/lessons/84512

#좀 무식한 방법... 글자가 5개밖에 안되니까 가능한것
def solution(s):
    answer = 0

    words = []
    box = ['A','E','I','O','U']
    word = ['','','','','']
    for a in box:
        word[0] = a
        words.append(''.join(word))
        for b in box:
            word[1] = b
            words.append(''.join(word))
            for c in box:
                word[2] = c
                words.append(''.join(word))
                for d in box:
                    word[3] = d
                    words.append(''.join(word))
                    for e in box:
                        word[4] = e
                        words.append(''.join(word))
                    word[4] = ''
                word[3] = ''
            word[2] = ''
        word[1] = ''
    answer = words.index(s) + 1
    return answer

#다른답: 해당문자열이 될때까지 문자열을 모음사전 순서대로 A, AA, AAA... 순서로 count를 1씩해가며 만들어간다
def solution1(word, cnt=1):
    w={'A':'E','E':'I','I':'O','O':'U','U':0}
    def nxt(i):
        if w[i[-1]]:
            return i[:-1]+w[i[-1]]
        else: 
            return nxt(i[:-1])
    i='A'
    while i!=word:
        if len(i)<5:
            i+='A'
            print(i)
        elif i[-1]:
            i=nxt(i)
            print(i)
        cnt += 1
    return cnt

print(solution1("AAAE"))