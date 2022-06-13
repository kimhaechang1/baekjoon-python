def solution(a,b,c):
    hour = a
    min = b+c
    if b+c>=60:
        hour+=(b+c)//60
        min = (b+c)%60
    if hour>=24:
        hour %=24

    return str(hour)+" "+str(min)


a, b = map(int,input().split())
c = int(input())

print(solution(a,b,c))