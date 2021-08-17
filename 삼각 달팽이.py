def solution(n):
    answer = []
    
    pyramid = [[] for _ in range(n)]
    
    height = 0
    bottom = n-1
    down = True
    thick = 0
    for i in range(1, int(n*(n+1)/2)+1):
        if down and height == bottom and len(pyramid[height]) < bottom + 1:
            pyramid[height].insert(len(pyramid[height])-thick,i)
            if len(pyramid[height]) == bottom + 1:
                down = False
                height -= 1
                bottom -= 1
        
        elif not down:
            pyramid[height].insert(len(pyramid[height])-thick,i)
            if len(pyramid[height]) == height + 1:
                down = True
                height += 1
                thick += 1
            else: 
                height-=1
        
        else:
            pyramid[height].insert(thick,i)
            height+=1
            
    print(pyramid)
    
    for j in pyramid:
        answer = answer + j
    
    return answer

n = 5
print(solution(n))

#다른답
def solution1(n):
    #오른쪽이동, 아래로이동, 좌상단으로 이동
    dx=[0,1,-1] 
    dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)] #피라미드 모양으로 0을 배열
    x,y=0,0
    num=1
    d=0
    while num<=(n+1)*n//2:
        b[y][x] = num
        ny = y + dy[d]
        nx = x + dx[d]
        num += 1
        #다음 이동할칸이 피라미드범위 내에 있으며, 이동가능한(0)경우
        if 0 <= ny < n and 0 <= nx <= ny and b[ny][nx]==0:
            y,x=ny,nx
        #그렇지않을경우 다음칸으로 이동할 곳을 지정하는 d의값을 바꾼다
        else:
            d = (d+1) % 3
            y += dy[d]
            x += dx[d]
        print(b)
    return sum(b,[])

n = 5
print(solution1(n)) 