def recu(n,a,b,c):
    if  n == 1:
        print(a,c)
    else:
        recu(n-1,a,c,b)
        print(a,c)
        recu(n-1,b,a,c)
def solution(n):
    recu(n,1,2,3)
n = int(input())
print(2**n-1)
solution(n)
