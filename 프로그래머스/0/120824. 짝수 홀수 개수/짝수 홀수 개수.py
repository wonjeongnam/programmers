def solution(num_list):
    even = 0
    odd = 0
    for i in range(0, len(num_list)):
        if num_list[i] % 2 ==0:
            even = even + 1
        else:
            odd = odd +1
    return([even, odd])