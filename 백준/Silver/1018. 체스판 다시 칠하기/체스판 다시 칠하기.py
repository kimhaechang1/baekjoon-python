def chk(i,k,m):
    fw= 0
    fb = 0
    for n in range(i,i+8):
        for j in range(k,k+8):

            if (n+j) %2 == 0: #(0,2)(0,4) (2,0)
                # 시작이 w인 경우
                if m[n][j] != "W":
                    fw+=1
                # 시작이 B인 경우
                if m[n][j] !="B":
                    fb +=1
            else: #(0,1)
                # 시작이 w인 경우
                if m[n][j] !="B":
                    fw+=1
                # 시작이 B인 경우
                if m[n][j] !="W":
                    fb+=1
    return fw, fb


def solution(N,M,m):
    result = []
    for i in range((N-8)+1):
        for k in range((M-8)+1):
            a1, a2 = chk(i,k,m)
            result.append(a1)
            result.append(a2)
    print(min(result))
N, M = map(int,input().split())
m = []
for i in range(N):
    m.append(list(map(str,input())))

solution(N,M,m)