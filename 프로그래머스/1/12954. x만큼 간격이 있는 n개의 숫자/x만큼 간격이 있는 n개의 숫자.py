# def solution(x, n):
#     if x >= 0:
#         answer = [i for i in range(x,x*n+1,x)]
#     else:
#         answer = [i for i in range(x,x*n-1,x)]
#     return answer

def solution(x, n):
    list1 = [i for i in range(1, n+1)]
    answer = [i * x for i in list1]
        
    return answer