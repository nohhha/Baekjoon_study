def solution(brown, yellow):
    answer = []
    for y in range(1, int(yellow**0.5)+1):
        if yellow%y==0:
            if (y+yellow//y+2)*2==brown:
                answer=[yellow//y+2, y+2]
                break
    return answer