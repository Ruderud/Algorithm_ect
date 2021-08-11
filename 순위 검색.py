# https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):

  #모든 조합경우에 대한 dict배열을 만들어놓음
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    #지원자들 정보를 공백을 기준으로 단어단위로 나누고, 이를 위의 data배열에 배정한다. 이떄 '-'로 지정한 값에도 지정하기에 한지원의 값이 총 2*4 번 입력된다.
    for i in info:
        i = i.split()
        print(i)
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        #해당 data[key] 의 value에 해당하는 배열에 점수를 추가하는형식 => 동점자수를 카운트 가능
                        data[(a, b, c, d)].append(int(i[4]))

    

    for k in data:
        #각 항목별 점수를 오름차순으로 정렬
        data[k].sort()

        # print(k, data[k])

    answer = list()
    #이진검색을 이용해서 해당 pool을 key로 하는 data의 value에 찾아간 후, 해당 점수배열을 이진검색을 통해 갯수를 찾는다 => bisect를 이용하면 더 간단하게 줄일 수 있음.
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))