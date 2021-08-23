# https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    cal_table = []
    for line in table:
        cal_table.append(list(line.split(' ')))
    
    cal_table.sort(key = lambda x : x[0])

    recommend = ['', 0]

    for corp in cal_table:

        score = 0
        for skill, prf in zip(languages, preference):
            if skill in corp:
                score += prf * (6 - corp.index(skill))
            else:
                continue

        if score > recommend[1]:
            recommend = [corp[0], score]

    return recommend[0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7,5,5]
print(solution(table,languages,preference))

#다른답
def solution1(table, languages, preference):
    answer = 'ZZZZZZZZ'
    #언어 : 선호도로 dict를 구성한후, 각 테이블값과 계산 비교하여 최대값을 갱신하면서 추천회사를 선정
    score_dic = {lang: score for lang, score in zip(languages, preference)}
    max_score = 0
    for row in table:
        r = row.split(' ')
        curr_score = 0
        for i in range(1, len(r)):
            curr_score += score_dic.get(r[i], 0) * (6-i)
        if max_score < curr_score:
            max_score = curr_score
            answer = r[0]
        elif max_score == curr_score and answer > r[0]:
            answer = r[0]


    return answer

print(solution1(table,languages,preference))