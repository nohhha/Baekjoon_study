from itertools import permutations

def solution(numbers):
    answer = []
    nums=list(numbers)
    per=[]
    
    for i in range(1, len(nums)+1):
        per += list(permutations(numbers, i))
    new_nums = list(set([int("".join(p)) for p in per]))
    
    for n in new_nums:
        if n<2:
            continue
        check=True
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                check=False
                break
        if check:
            answer.append(n)
    
    return len(set(answer))