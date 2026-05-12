N,M = map(int, input().split())
n = N//2
i = 0
while i <= n:
    c = '.l.'
    i = (2*n*c + c).center(M,'-')
    print(i)
    i +=1
    break