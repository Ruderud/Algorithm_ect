#https://programmers.co.kr/learn/courses/30/lessons/77484

#이진검색 쓸필요도없음 -> 기껏해봐야 숫자 6개쓰니까
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19] #result: [3,5]

def solution(lottos, win_nums):
    answer = []

    rank = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }    #index를 맟춘갯수로 하여 등수를 매기면 rank = [6,6,5,4,3,2,1]로해서 더 깔끔하게 가능했음
    joker = lottos.count(0)
    correct = 0
    
    for num in win_nums:
        if num in lottos:
            correct+=1
        else:
            continue
    
    answer.append(rank[correct+joker])
    answer.append(rank[correct])

    return answer

print(solution(lottos,win_nums))

