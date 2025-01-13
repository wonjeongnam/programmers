def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer =sum(num_list)
        return answer
    else:
        for i in range(len(num_list)):
            answer = answer * num_list[i]
        return answer