def solution(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        average = sum / len(numbers)
    return average
