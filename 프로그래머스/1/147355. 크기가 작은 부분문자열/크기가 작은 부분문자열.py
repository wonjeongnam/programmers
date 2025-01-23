def solution(t, p):
    answer = []
    for i in range(len(t)):
        slice = t[i:i+len(p)]
        if len(slice) == len(p):
            if slice <= p:
                answer.append(slice)
    return (len(answer))
    