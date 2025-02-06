def solution(number):
    result = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for z in range(j+1, len(number)):
                if number[i] + number[j] + number[z] == 0:
                    result += 1
    return result