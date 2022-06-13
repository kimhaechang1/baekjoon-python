def fibo(n):
    dp = [0,1]
    if  n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
    return dp
def solution(n):
    answer= fibo(n)
    answer = answer[len(answer)-1]
    return answer


print(solution(int(input())))