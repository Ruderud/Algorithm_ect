# https://programmers.co.kr/learn/courses/30/lessons/42583

#stack적인 요소가 하나도없기때문에 매우 빠름
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    bridge_weight = 0
    bridge_trucks = 0
    while q or bridge_trucks:
        if bridge_trucks:
            a = bridge.popleft()
            if a:
                bridge_weight -= a
                bridge_trucks -= 1
            answer+=1
            # print(bridge)
            # print(len(bridge), answer)

            if q and bridge_weight + q[0] <= weight:
                b = q.popleft()
                bridge.append(b)
                bridge_trucks += 1
                bridge_weight += b
                # print(bridge)
                # print(len(bridge), answer)
            else:
                bridge.append(0)

        else:
            c = bridge.popleft()
            if c:
                bridge_trucks -= 1
                bridge_weight -= c
            d = q.popleft()
            bridge.append(d)
            bridge_trucks += 1
            bridge_weight += d
            answer+=1
            # print(bridge)
            # print(len(bridge), answer)
        
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))

#다른답 : reverse를 통해 스택이지만 뒤에서 부터 빼는 방식을 활용
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step