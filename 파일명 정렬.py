# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = []
    
    nums = [str(i) for i in range(10)]
    files_sep = []
    for file in files:
        file += '!'
        box = []
        numscan = False
        num_p = 0
        for p in range(len(file)):
            if file[p] in nums and not numscan:
                box.append(file[:p])
                num_p = p
                numscan = True
            elif file[p] not in nums and numscan:
                box.append(file[num_p:p])
                box.append(file[p:-1])
                break
        
        box.append(box[0].lower())
        files_sep.append(box)
            
    
    print(files_sep)
    files_sep.sort(key = lambda x: (x[-1], int(x[1]) ))
    
    for file_sep in files_sep:
        answer.append(''.join(file_sep[0:-1]))
    
    return answer

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", 'q1']
print(solution(files))


#다른답: 정규식 사용
import re

def solution(files):
    #숫자 우선으로 정렬(\d+ => 숫자문자열을 가져와서 int화)
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    #정렬한 a를 다시 문자를 우선으로 정렬. 이떄 가져온 문자는 lower()을 통해 소문자기준으로 정렬
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b