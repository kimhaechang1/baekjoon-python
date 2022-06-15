import sys
result = []
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    sam = sorted([a,b,c])

    if sam[0]**2 + sam[1]**2 == sam[2]**2:
        result.append("right")
    else:
        result.append("wrong")

for p in result:
    print(p)