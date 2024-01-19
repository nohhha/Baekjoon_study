def solution(sizes):
    answer = 0
    max_x,max_y=0,0
    new_sizes=[]
    for i, size in enumerate(sizes):
        if size[0]<size[1]:
            size=[size[1], size[0]]
        if size[0]>max_x:
            max_x=size[0]
        if size[1]>max_y:
            max_y=size[1]
        answer = max_x*max_y
    return answer