def make(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((max)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j] = False
    return isPrime

def solution(numbers):
    for num in numbers:
        temp = make(num*2)
        c = 0
        for i in temp[num+1:2*num+1]:
            if i:
                c+=1
        print(c)
n =[]
while True:
    t= int(input())
    if t == 0:
        break
    else:
        n.append(t)
solution(n)