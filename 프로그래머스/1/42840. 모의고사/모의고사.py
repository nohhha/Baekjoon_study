def solution(answers):
    answer = []
    way1=[1,2,3,4,5]*2000
    way2=[2,1,2,3,2,4,2,5]*1250
    way3=[3,3,1,1,2,2,4,4,5,5]*1000
    ways=[way1, way2, way3]
    max_cnt=0
    for i, way in enumerate(ways):
        way=way[:len(answers)]
        count = sum(a==b for a, b in zip(way, answers))
        if count>max_cnt:
            answer=[]
            answer.append(i+1)
            max_cnt=count
        elif count==max_cnt:
            answer.append(i+1)
    
    return answer