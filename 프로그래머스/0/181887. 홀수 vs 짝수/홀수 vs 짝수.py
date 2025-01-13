def solution(num_list):
    answer1= [num_list[i] for i in range(len(num_list)) if i % 2 != 0]
    answer2= [num_list[i] for i in range(len(num_list)) if i % 2 == 0]
    if sum(answer1) > sum(answer2):
        return sum(answer1)
    else:
        return sum(answer2)