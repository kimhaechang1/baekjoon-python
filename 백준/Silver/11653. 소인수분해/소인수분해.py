def make(n):
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    prime = []
    for i in range(2, int((n+1)**(1/2))):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j] = False
    for i in range(n+1):
        if isPrime[i] :
            prime.append(i)
    return prime

def solution(n):
   if n == 1:
       return
   else:
    p = make(n)
    k = 0
    while True:
        if n == 1:
            break
        elif n % p[k] == 0:
            n = n / p[k]
            print(p[k])
        else:
            k+=1



solution(int(input()))