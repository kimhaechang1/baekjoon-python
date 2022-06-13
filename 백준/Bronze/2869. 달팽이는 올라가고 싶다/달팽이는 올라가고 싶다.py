def solution(a,b,v):
    if (v -b)%(a-b) == 0:
        answer =(v -b)//(a-b)
    else:
        answer = (v-b)//(a-b)+1
    return answer

A,B,V = map(int,input().split())
print(solution(A,B,V))