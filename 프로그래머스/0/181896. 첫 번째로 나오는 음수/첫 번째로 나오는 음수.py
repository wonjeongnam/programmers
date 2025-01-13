def solution(num_list):
    if all(i > 0 for i in num_list) == True:
        return -1
    else:
        for i in range(len(num_list)):
            if num_list[i] < 0 :
                return i

