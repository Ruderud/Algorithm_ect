# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def notUnique(nowComb, uniqueCombs):    #현재조합의 부분집합중에 유니크한 키가있는지 확인하는 함수
    for uniComb in uniqueCombs:
        count = 0
        for uniEle in uniComb:
            if uniEle in nowComb:
                count+=1
        if count == len(uniComb):
            return True
    return False

def solution(relation):
    AllCombinations = []
    for num in range(1, len(relation[0])+1):    #1명에대한 데이터가 n개있을때, 1개부터 n개까지 뽑아서 만드는 조합 종류 만들기
        for comb in list(combinations(range(len(relation[0])),num)):
            AllCombinations.append(comb)

    uniqueComb = []

    for combination in AllCombinations:
        keys=[]
        if notUnique(combination, uniqueComb):  #유니크조합에 있는조합이 현재의 조합내에 있다면 패스
            continue

        for person in relation:           #조합을 하나씩 가져와서 키를 만들고, 유일성이 보장되는지 확인
            key = []
            for site in combination:
                key.append(person[site])
            keys.append(tuple(key))

        if len(keys) == len(set(keys)):     #set을 사용하여 유일성확인
            uniqueComb.append(combination)
            
    return len(uniqueComb)