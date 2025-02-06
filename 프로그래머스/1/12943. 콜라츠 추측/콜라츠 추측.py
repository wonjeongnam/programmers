def solution(num):
    i = 0
    if num == 1:
        return(i)
    else:   
        while i < 500 :
            if num % 2 == 0:
                num = num // 2
                i += 1
            else:  
                num = num * 3 + 1
                i += 1
            if num == 1:
                break
            if i == 500:
                return -1
        return(i)
    