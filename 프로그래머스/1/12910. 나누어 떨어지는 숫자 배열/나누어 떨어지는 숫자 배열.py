def solution(arr, divisor):
    answer = [ i for i in arr if i % divisor == 0]
    if answer == []:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer