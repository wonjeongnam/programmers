def solution(money):
    b=[ i for i in range(1000000) if 5500*i <= money]
    answer = b[-1],money-5500*b[-1]
    return answer