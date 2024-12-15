def solution(array, height):
    count=0
    for i in range(0,len(array)):
        if height < array[i]:
            count=count+1
    return count
