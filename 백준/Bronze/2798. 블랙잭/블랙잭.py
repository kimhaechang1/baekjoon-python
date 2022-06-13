import itertools
def solution(n, m,c):
    hap = []
    abso = []
    for i in list(itertools.combinations(c,3)):
        if sum(i)>m:
            continue
        hap.append(sum(i))

        abso.append(m - sum(i))
    if m-min(abso) in hap :
        answer = m-min(abso)
    return answer

n, m  = map(int, input().split())
c = list(map(int, input().split()))
print(solution(n,m, c))
