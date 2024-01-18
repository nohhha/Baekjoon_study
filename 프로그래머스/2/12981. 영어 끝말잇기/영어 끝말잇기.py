def solution(n, words):
    answer = []
    wordslist=[]
    i=0
    while True:
        person = i%n+1
        cnt = (i//n)+1
        if i==len(words):
            break
        if words[i] in wordslist:
            break
        else:
            wordslist.append(words[i])
        if i>0 and words[i-1][-1] != words[i][0]:
                break
        i+=1
    if i==len(words):
        answer=[0,0]
    else:
        answer=[person, cnt]
    

    return answer