import sys

n = int(sys.stdin.readline())
words = set()
k = [""]*51
for i in range(n):
    words.add(sys.stdin.readline().strip())
words = list(words)

for i in words:
    k[len(i)]+=i+" "

for w in k:
    w = w.split()
    w = sorted(w)
    for m in w:
        print(m)