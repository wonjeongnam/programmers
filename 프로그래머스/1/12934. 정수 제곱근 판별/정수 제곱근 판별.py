def solution(n):
    x = int(n ** (1/2))
    if x ** 2 == n:
        answer = int((x+1) ** 2)
        return answer
    else:
        return -1
    