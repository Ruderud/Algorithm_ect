# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []

    #기본사전생성
    dic = {}
    for i in range(65,91):
        dic[chr(i)] = i-64
    
    print(dic.keys())
    
    dic_num = 27
    p=0
    while p < len(msg):
        check = msg[p]

        pp = p+1
        print(p,'번째 글자 검사중',check[p:pp])

        while msg[p:pp] in dic.keys():
            print("문장검사", check[p:pp], pp)
            pp += 1
            if pp >= len(msg):
                pp += 1
                break
        
        print(msg[p:pp-1])
        print(msg[p:pp-2])
        print(dic)

        if msg[p:pp-1] in dic.keys():
            answer.append(dic[msg[p:pp-1]])
            dic[msg[p:pp]] = dic_num
        else:
            answer.append(dic[msg[p:pp-2]])
            answer.append(dic[msg[pp-2:pp-1]])
            dic[msg[p:pp-1]] = dic_num
        dic_num += 1
        p = pp-1

    return answer

# msg = "ABABABABABABABAB"
msg = "KAKAO"
print(solution(msg))


#다른답
def solution(msg):
    answer = []
    #dict도 list comprehansion 문장 형태로 가능
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        #검사가 끝난 만큼의 글자를 제외한 나머지만을 슬라이싱처리
        msg = msg[tt:]
    return answer