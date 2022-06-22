import sys
result = []
while(True):
    a1,a2 = map(int, sys.stdin.readline().split())
    if a1 == a2 == 0 :
        break
    elif a2 % a1 == 0:
        result.append("factor")
    elif a1 %a2 == 0:
        result.append("multiple")
    else:
        result.append("neither")

for r in result:
    print(r)