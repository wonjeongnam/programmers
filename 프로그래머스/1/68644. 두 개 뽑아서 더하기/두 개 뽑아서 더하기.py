def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            answer.append(result)
    answer = sorted(set(answer))     
    return answer