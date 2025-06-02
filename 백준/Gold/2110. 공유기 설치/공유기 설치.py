N, C = map(int, input().split()) # N: 집 개수, C: 공유기 개수
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

def binary_search(start, end):
    while start<=end:
        curr = arr[0] # 현재 집 위치
        count = 1
        mid = (start+end)//2 # 가장 인접한 두 공유기 사이 최대 거리 설정

        for i in range(1, N):
            if arr[i]>=curr+mid:
                curr = arr[i] # i번째 집 위치에 공유기 설치
                count +=1
        if count>=C: # 최대 거리 늘리기
            global ans
            ans = mid
            start = mid+1
        else: #최대 거리 줄이기
            end = mid-1

ans = 0
start, end = 1, arr[-1]-arr[0] # 공유기 사이 거리 최소값(1), 최대값(가장 먼 집 - 가장 가까운 집)
binary_search(start, end)
print(ans)