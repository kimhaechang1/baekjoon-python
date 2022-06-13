import sys
import collections

def avg(l,n):
    print(round(sum(l)/n))

def mid(l,n):
    l = sorted(l)
    print(l[n//2])

def fre(l,n):
    ld = collections.Counter(l)
    m2 = max(ld.values())
    ld = sorted(ld.items(), key = lambda x : x[1], reverse=True)
    m1 = ld[0][1]
    temp = []
    for key, value in ld :
        if m1 == value:
            temp.append(key)
    temp = sorted(temp)
    if len(temp)>1:
        print(temp[1])
    else:
        print(temp[0])

def bound(l):
    print(max(l)-min(l))


n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline().strip()))

avg(l,n)
mid(l,n)
fre(l,n)
bound(l)