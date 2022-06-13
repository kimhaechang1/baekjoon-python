def make(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    p = []
    for i in range(2, int((max)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j]= False
    for i in range(max+1):
        if isPrime[i]:
            p.append(i)
    return p
def solution(m,n):
    p = make(n)
    for i in p:
        if i >=m and i<=n:
            print(i)


m, n = map(int, input().split())
solution(m, n)