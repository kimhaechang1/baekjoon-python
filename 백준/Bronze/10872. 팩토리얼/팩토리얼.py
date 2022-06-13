def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
def solution(n):
    answer = fact(n)
    return answer

print(solution(int(input())))