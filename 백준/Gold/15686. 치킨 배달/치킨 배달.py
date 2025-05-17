from itertools import combinations

N,M = map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            chickens.append((i,j))
        if arr[i][j]==1:
            houses.append((i,j))

def cal_dist(chickens):
    total_dist = 0
    for hi,hj in houses:
        min_dist = 2*N
        for ci,cj in chickens:
            dist = abs(ci-hi)+abs(cj-hj)
            min_dist = min(min_dist,dist)
        total_dist += min_dist

    return total_dist

def main():
    min_dist = len(houses)*2*N
    for chkn in combinations(chickens, M):
        dist = cal_dist(chkn)
        min_dist = min(min_dist, dist)

    print(min_dist)

main()