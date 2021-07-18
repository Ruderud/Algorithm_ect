# https://leetcode.com/problems/average-waiting-time/

def sol(customers):

    work_flow = []
    wait=[]

    for arrive, work in customers:
        if not work_flow:
            work_flow = [arrive,arrive+work]
            wait.append(work)
        
        else:
            if arrive < work_flow[1]:
                work_flow = [arrive,work_flow[1]+work]
                wait.append(work_flow[1]-work_flow[0])
            
            else:
                work_flow = [arrive,arrive+work]
                wait.append(work)

    return sum(wait)/len(customers)


# customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
print(sol(customers))
