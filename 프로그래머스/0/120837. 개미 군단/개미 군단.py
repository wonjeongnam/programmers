def solution(hp):
    x = hp // 5
    y = (hp % 5) // 3
    z = (hp % 5) % 3
    answer = x + y + z

    return answer