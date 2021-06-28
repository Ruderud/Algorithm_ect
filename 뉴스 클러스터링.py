# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    #알파벳을 전부 대문자화
    upper_str1 = str1.upper()
    upper_str2 = str2.upper()
    j_str1 = []
    j_str2 = []

    #2개씩연속해서 묶을때 알파벳인 요소만 리스트에 넣음
    for i in range(len(upper_str1)-1):
        if ord(upper_str1[i]) in range(65,91) and ord(upper_str1[i+1]) in range(65,91):
            j_str1.append(upper_str1[i]+upper_str1[i+1])
    for i in range(len(upper_str2)-1):
        if ord(upper_str2[i]) in range(65,91) and ord(upper_str2[i+1]) in range(65,91):
            j_str2.append(upper_str2[i]+upper_str2[i+1])


    common_s = 0
    all_s = 0
    #str1, str2의 각 요소의 중복을 제거한 합집합을 만든다
    all_ele = set(j_str1) | set(j_str2)

    #합집합의 요소하나씩 가져와서, 각 str의 요소리스트중 더 작은값들을 더해서 교집합 갯수를/ 더 큰값들을 더해서 합집합 갯수를 센다
    for ele in all_ele:
        common_s += min(j_str1.count(ele), j_str2.count(ele))
    for ele in all_ele:
        all_s += max(j_str1.count(ele), j_str2.count(ele))

    #만일 합집합의 갯수가 0인경우는 별도로 지정
    if all_s == 0 :
        return 65536
    else:
        return int(common_s/all_s * 65536)

str1, str2 = "aaaaa", "bbaa"
print(solution(str1, str2))

