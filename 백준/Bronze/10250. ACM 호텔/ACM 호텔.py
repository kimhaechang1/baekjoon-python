def solution(h,w,n):
    answer = 0
    if n%h == 0:
        answer+=h*100
        answer+=(n//h)
    else:
        if h<n:
            answer+=n%h*100
            answer+=(n//h)+1
        elif h>n:
            answer+=n*100
            answer +=1
    return str(answer)



T = int(input())
result = []
for i in range(T):
    h,w,n = map(int, input().split())
    result.append(solution(h,w,n))
for k in result:
    print(k)