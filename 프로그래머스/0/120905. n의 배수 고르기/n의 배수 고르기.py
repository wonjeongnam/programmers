def solution(n, numlist):
    answer=[numlist[i] for i in range(0,len(numlist)) if numlist[i] % n ==0]
    return answer