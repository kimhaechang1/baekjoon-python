def prime(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((max+1)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j] = False
    return isPrime

def solution(list):
    n = list[0]
    m = list[1]
    l= prime(m)
    p= []
    for i in range(n, m+1):
        if l[i]:
            p.append(i)
    if len(p) == 0:
        print(-1)
    else:
        print(sum(p))
        print(min(p))


n = []
for i in range(2):
    n.append(int(input()))

solution(n)