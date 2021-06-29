# https://programmers.co.kr/learn/courses/30/lessons/72411

#course 최대값의 숫자만큼 조합을 넣을 공간을 먼저 만든다. 
#이후 orders의 각 order에 대해 course 길이만큼의(2,3,4...len(order)->최대) combination을 각 공간에 집어넣는다
#이후 each_order_comb에서 요구하는 course의 값에 해당하는 index에서 가장 많이 count 된것을 결과에 집어넣고, 결과를 sort처리하여 반환


# from itertools import combinations

# def solution(orders, course):
#     answer = []

#     max_len_order = 0
#     for order in orders:
#         max_len_order = max(max_len_order, len(order))

#     each_order_comb = [[] for _ in range(max(course)+1)]
#     select_order_comb = [[] for _ in range(max(course)+1)]

#     for order in orders:
#         for length in course:
#             for comb in list(combinations(order,length)):
#                 each_order_comb[length].append(set(comb))

#     for cos in course:
#         if cos>max_len_order:
#             continue

#         cos_type = []
#         for i in each_order_comb[cos]:
#             if i not in cos_type:
#                 cos_type.append(i)

#         for type in cos_type:
#             n = each_order_comb[cos].count(type)
#             select_order_comb[cos].append((n,type))

#         select_order_comb[cos].sort(reverse=True)

#         if select_order_comb[cos][0][0] != 1:
#             answer.append(''.join(sorted(select_order_comb[cos][0][1])))

#             index = 1
#             while len(select_order_comb[cos])>1 and select_order_comb[cos][0][0] == select_order_comb[cos][index][0]:
#                 answer.append(''.join(sorted(select_order_comb[cos][index][1])))
#                 index+=1

#     return sorted(answer)


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)   #조합을 만들때 알파벳 오름차순으로 형성
        
        print('order_combinations: ',order_combinations)

        #most_common은 주어진 배열리스트를 받아서 -> ('원소', 원소가 등장하는 횟수)로 반환한다. 이때 ()에 숫자를 입력하면 내림차순으로 입력한 수만큼 출력
        most_ordered = collections.Counter(order_combinations).most_common()

        print('most_ordered: ',most_ordered)

        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]


# orders, course = ["ABCFG"], [2,3,4]
# orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
# orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]

print(solution(orders, course))

