# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):

    raw = s.lower().split(' ')
    answer = []
    for sen in raw:
        if len(sen) > 1:
            answer.append(sen[0].upper() + sen[1:])
        else:
            answer.append(sen.upper())

    return ' '.join(answer)

#다른답
def solution(s):
    #" "으로 해야 공백 한칸을 기준으로 정확히 나눌 수 있음
    #capitalize()는 모든 아스키 문자의 첫번째는 대문자, 나머지는 소문자로 반환. 비슷한 메서드로 title()이 있음
    return ' '.join([word.capitalize() for word in s.split(" ")])