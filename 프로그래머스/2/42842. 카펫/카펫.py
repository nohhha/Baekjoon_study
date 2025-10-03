def solution(brown, yellow):
    answer = []
    
    h = 1
    while True:
        if yellow%h == 0:
            w = yellow//h
            if ((w+2)*(h+2)) == (yellow+brown):
                return [w+2, h+2]
            else:
                h += 1
        else:
            h += 1
    
    return answer