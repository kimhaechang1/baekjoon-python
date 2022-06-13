import sys

n = int(sys.stdin.readline())

age = [""]*201

for i in range(n):
    a, t = sys.stdin.readline().split()
    age[int(a)]+=t+" "

for i in range(201):
    if age[i]=="":
        continue
    ms = age[i].split()
    for m in ms:
        print(i, m)