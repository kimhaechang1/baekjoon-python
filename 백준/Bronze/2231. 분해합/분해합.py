def solution(n):
    answer = 0
    for i in range(1,n+1):
        a = list(map(int, str(i)))
        p = i + sum(a)
        if p == n:
            answer = i
            break
    return answer



print(solution(int(input())))