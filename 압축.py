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