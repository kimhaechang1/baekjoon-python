def solution(l):
    result = []

    for i in range(len(l)) :
        index = i
        px, py  = l[i]
        rank=1
        for k in range(len(l)):
            if index == k:
                continue
            xx, yy = l[k]
            if px<xx and py<yy:
                rank+=1
        result.append(rank)

    return result


N = int(input())
l = []
for i in range(N):
    x,y = map(int,input().split())
    l.append((x,y))

t = solution(l)
for i in t:
    print(i,end=" ")