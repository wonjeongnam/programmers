def solution(arr):
    if arr == [] or len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr