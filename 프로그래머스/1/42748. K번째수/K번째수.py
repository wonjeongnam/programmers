def solution(array, commands):
    result = []
    for i in range(len(commands)):
        answer = sorted(array[commands[i][0]-1:commands[i][1]])
        commands_last = commands[i][2]
        result.append(answer[commands_last-1])
    return result