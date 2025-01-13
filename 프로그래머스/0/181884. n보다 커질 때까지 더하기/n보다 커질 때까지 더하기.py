def solution(numbers, n):
    answer_sum = 0
    for i in numbers:
        if answer_sum <= n:
            answer_sum += i

    return answer_sum