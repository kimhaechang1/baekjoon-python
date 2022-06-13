def makePrime():
    isPrime = [True]*1001
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2,int((1001)**(1/2))):
        if isPrime[i]:
            for j in range(i+i,1001,i):
                isPrime[j] = False
    return isPrime
def solution(numbers):
    l = makePrime()
    answer = 0
    for num in numbers:
        if l[num]:
            answer +=1
    return answer


N = int(input())
l = list(map(int, input().split()))

print(solution(l))