def solution(sides):
    sides.sort()
    if sum(sides[:2]) > sum(sides[-1:]):
        return 1
    else: 
        return 2