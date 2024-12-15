import math 
def solution(n):
    if n % math.sqrt(n) != 0:
        return 2
    else:
        return 1
    