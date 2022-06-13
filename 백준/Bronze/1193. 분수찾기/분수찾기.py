def solution(x):
    p = 0
    answer=""
    while True :
        if x<=0:
            break
        else:
            p += 1
            x-=p
    q = [x for x in range(1,p+1)]
    if p%2==0:
        answer+=str(q[-1+(x)])+"/"+str(q[0+(x*-1)])
    else:
        answer+=str(q[0+(x*-1)])+"/"+str(q[-1+(x)])
    return answer


X = int(input())
print(solution(X))