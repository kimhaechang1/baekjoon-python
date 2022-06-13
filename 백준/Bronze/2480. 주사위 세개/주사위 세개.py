import collections
def solution(d):
    answer = 0
    d_set = set(d)
    if len(d_set)==1:
        answer = 10000+d_set.pop()*1000
    elif len(d_set)==2:
        t = collections.Counter(d)
        for key, value in t.items():
            if value==2:
                answer = 1000+ key*100
    else:
        answer = max(d)*100
    return answer


dice = list(map(int, input().split()))
print(solution(dice))