def solution(arr1, arr2):
    result = [i[:] for i in arr1]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            result[i][j] = arr1[i][j]+arr2[i][j]
    return result