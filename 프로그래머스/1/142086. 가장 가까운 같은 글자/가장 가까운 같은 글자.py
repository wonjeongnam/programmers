def solution(s):
    s= list(s)
    tmp = []
    result = []
    for idx, val in enumerate(s):
        if val in tmp:
            result.append(idx - s.index(val))
            s[s.index(val)] = ''

        else:
            tmp.append(val)
            result.append(-1)
    return result    