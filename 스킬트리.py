#https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        root = []
        for i in range(len(skill)):
            if skill[i] not in skill_tree:
                root.append(30)
            else:
                root.append(skill_tree.find(skill[i]))

        if root == sorted(root):
            answer+=1
        
    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA", "TTTT"]
# print(solution(skill, skill_trees))



#따봉해답 : 
def solution1(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        

        for s in skills:
            print(s)
            if s in skill:
                if s != skill_list.pop(0):  #선행 맨앞스킬부터 빠지지않게되면 break로 넘어간다
                    break
        else:   #for문중에 break로 끊기지 않으면 else문장이 실행되는 for-else문 방법
            answer += 1

    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA", "TTTT"]
print(solution1(skill, skill_trees))