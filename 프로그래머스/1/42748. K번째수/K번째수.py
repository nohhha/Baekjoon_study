def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new = array[i-1:j]
        print(new)
        new.sort()
        print(new)
        answer.append(new[k-1])
    return answer