def solution(n):
    j = 666
    cnt = 0
    while True:
        if "666" in str(j):
            cnt+=1
        if n == cnt:
            print(j)
            break
        j+=1


solution(int(input()))