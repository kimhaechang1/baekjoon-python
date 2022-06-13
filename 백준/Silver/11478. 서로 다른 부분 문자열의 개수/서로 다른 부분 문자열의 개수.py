import sys

words = sys.stdin.readline().strip()
set_words = set()

for l in range(1, len(words)+1):
    for k in range(len(words)):
        if k+l> len(words):
            break
        set_words.add(words[k:k+l])

print(len(set_words))