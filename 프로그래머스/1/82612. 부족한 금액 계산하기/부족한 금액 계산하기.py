def solution(price, money, count):
    p_c = list(range(price,price*count+1,price))
    answer = sum(p_c) - money
    if answer < 0 :
        return 0
    else:
        return answer
