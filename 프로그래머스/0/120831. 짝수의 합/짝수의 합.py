def solution(n):
    sum = 0
    a = n//2
    for i in range(1,a+1):
        sum = sum + i
    return (2*sum)