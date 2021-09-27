def main():
    x = int(input())

    for _ in range(x):
        s = input()
        n = len(s)
        if n%2 == 1:
            # print(list(s[:(n//2)+1]), list(reversed(s))[:(n//2)+1] )
            if list(s[:(n//2)+1]) == list(reversed(s))[:(n//2)+1]:
                print('NO')
            else:
                print("YES")
        else:
            # print(list(s[:(n//2)]), list(reversed(s))[:(n//2)])
            if list(s[:(n//2)]) == list(reversed(s))[:(n//2)]:
                print('NO')
            else:
                print("YES")
                
if __name__=="__main__":
    main()

