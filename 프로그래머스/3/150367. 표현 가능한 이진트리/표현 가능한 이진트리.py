def dfs(i, num_bin, mid, h):
    if h==1:
        return
    
    global answer
    left = mid - 2**(h-2)
    right = mid + 2**(h-2)
    if num_bin[mid]=='0':
        if num_bin[left]=='1' or num_bin[right]=='1':
            answer[i] = 0
    
    if answer[i]==1:
        dfs(i, num_bin, left, h-1)
        dfs(i, num_bin, right, h-1)

        
def solution(numbers):
    global answer
    answer = [1]*len(numbers)
    for i in range(len(numbers)):
        num_bin = format(numbers[i], 'b')

        h = 1
        while True:
            if len(num_bin)<=2**h-1:
                break
            else:
                h += 1
        # 이진수 2**h-1 의 길이로 만들기 => 앞을 0으로 채워
        while len(num_bin)<2**h-1:
            num_bin = '0'+num_bin
        
        # 더미노드가 자식을 가지면 불가능
        mid = (0+len(num_bin)-1)//2
        dfs(i, num_bin, mid, h)
        
    
    return answer