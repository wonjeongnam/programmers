def solution(s):
    result = []
    s = s.split(' ')
    for i in range(len(s)):
        word = ""
        for j in range(len(s[i])):
            if j % 2 == 0 :
                word += s[i][j].upper()
            else:
                word += s[i][j].lower()
        result.append(word)
    return ' '.join(result)