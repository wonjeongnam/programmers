def solution(my_string, alp):
    if alp in my_string:
        c=my_string.find(alp)
        answer=my_string.replace(my_string[c],alp.upper())
    else: 
        answer=my_string
    return answer