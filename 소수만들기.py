#https://programmers.co.kr/learn/courses/30/lessons/12977

#input 원소중 1,2번쨰로 큰값의 합을 n이라 하고, n까지의 소수를 리스트로 만든다
# combination을 이용해서 nums중 3개를 고르는 조합리스트를 만들고, 조합의 수의 합이 소수에있으면(binary) count+1, 없다면 pass

from itertools import combinations

def primelist(n):
    if n == 1:
        return []
    else:
        p=3
        past=[2]
        while p<=n:
            avalable=True
            for i in past:
                if p%i==0:
                    avalable = False
                    break
            if avalable: past.append(p)
            p+=1
        return past

#소수판정법중 하나로써, 주어진수가 자연수 1보다 크고 루트n이하인 모든 자연수로 나누어떨어지지않으면 소수임.

def solution(nums):
    nums.sort()
    maxvalue = sum(nums[-3:])
    primenums = primelist(maxvalue)
    comb = list(combinations(nums,3))
    answer=0
    
    for c in comb:
        if sum(c) not in primenums:
            continue
        else:
            answer+=1

    return answer

nums = [1,2,3,4]

print(solution(nums))