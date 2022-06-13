T = int(input())
n = []
for i in range(T):
    n.append(int(input()))

def make(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((max)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j]=False
    return isPrime
def solution(numbers):
    for num in numbers:
        p = make(num)
        a,b = num//2, num//2
        for _ in range(len(p)//2):
            if p[a] and p[b]:
                print(a,b)
                break
            else:
                a -=1
                b +=1
solution(n)