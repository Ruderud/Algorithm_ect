#https://programmers.co.kr/learn/courses/30/lessons/12973

s = 'baabaa'

def solution(s):

    del_s = []
    del_s_c = 0

    for i in range(len(s)):
        del_s+=s[i]
        del_s_c+=1

        if del_s_c>=2 and del_s[-1] == del_s[-2]:
            del_s.pop()
            del_s.pop()
            del_s_c-=2

    if del_s:
        return 0
    else:
        return 1

print(solution(s))