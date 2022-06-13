def solution(k, n):
    answer = 0
    home = [[0]*n for _ in range(k+1)]
    for i in range(k+1):
        home[i][0]=1
    for i in range(1,n+1):
        home[0][i-1] = i
    if k>1:
        for i in range(1,k+1):
            for t in range(1,n):
                home[i][t] = home[i-1][t]+home[i][t-1]
        answer = home[k][n-1]
    else :
        p=[]
        for i in range(1,n+1):
            p.append(i)
        answer = sum(p)
    return answer
T = int(input())

r = []

for i in range(T):
    k = int(input())
    n = int(input())
    r.append(solution(k,n))

for k in r:
    print(k)