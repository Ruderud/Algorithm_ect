def main():
    x = int(input())
    
    for _ in range(x):
        n, m = map(int, input().split())
        array = set((i, i+1) for i in range(n-1))

        relation = set([])
        
        for _ in range(m):
            a,b = map(int, input().split())
            if a>b:
                relation.add((b,a))
            else:
                relation.add((a,b))
        
        # print(array)
        # print(relation)
        
        if array == relation:
            print(1)
        else:
            print(0)
        
        
        

if __name__=="__main__":
    main()
