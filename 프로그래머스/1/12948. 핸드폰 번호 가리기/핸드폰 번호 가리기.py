def solution(phone_number):
    answer = ["*" for i in phone_number[:-4]]
    answer2 = ''.join(answer) + phone_number[-4:]
    return answer2