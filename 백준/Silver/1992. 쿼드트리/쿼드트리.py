import sys
sys.setrecursionlimit(10**6)

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int, input())))

def quard(si,sj,size):
    if size==1:
        return str(arr[si][sj])
    else:
        num = arr[si][sj]
        string = ''
        for i in range(si,si+size):
            for j in range(sj,sj+size):
                if arr[i][j]!=num:
                    size //= 2
                    string += '('
                    string += quard(si,sj,size)
                    string += quard(si,sj+size, size)
                    string += quard(si+size,sj,size)
                    string += quard(si+size,sj+size,size)
                    string +=')'
                    return string
        # 숫자 모두 같으면 여기로
        return str(num)

ans = quard(0,0,N)
print(ans)