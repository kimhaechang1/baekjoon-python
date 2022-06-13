def solution(k):
    answer = 0
    if k%5 == 0:
        answer = k//5
    else:
        while k>0:
            k -=3
            answer+=1
            if k%5 == 0:
                answer+=k//5
                break
            elif k == 1 or k==2:
                answer = -1
                break
            elif k == 0:
                break
    return answer


print(solution(int(input())))