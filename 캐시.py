# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
        
    qcache = deque([])
    
    for city in cities:
        if city in qcache:
            num = qcache.index(city)
            qcache.append(city)
            del qcache[num]
            answer += 1
        
        else:
            qcache.append(city)
            if len(qcache) > cacheSize:
                qcache.popleft()
            answer += 5
    
    return answer

#다른답
def solution(cacheSize, cities):
    import collections
    #maxlen = num시, 이 큐는 num만큼의 크기만 가지게된다.
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time