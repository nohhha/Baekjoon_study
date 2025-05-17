import sys
input = sys.stdin.readline

N, init_atk = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split()))) # t, a, h
    # t==1: 몬스터 공격력==a, 생명력==h
    # t==2: 포션 존재, 용사의 공격력+=a, 현재 생명력=h

def check(mid):
    h_maxhp, h_curhp, h_atk = mid, mid, init_atk
    for ti,ai,hi in arr:
        if ti==1: # 몬스터 공격 횟수 cnt 구해서 몬스터 공격력 곱해서 용사 hp 죽이기
            cnt = hi//h_atk + (hi%h_atk>0) - 1
            h_curhp -= cnt*ai
        else: # 포션 먹기
            h_curhp = min(h_maxhp, h_curhp+hi)
            h_atk += ai
        if h_curhp<=0:
            return False
    return True

# 용을 쓰러트리기 위해 필요한 최소의 h_maxhp 찾기
# h_maxhp 범위를 이분 탐색
s = 1
e = int(1e18)
ans = 0
while (s<=e):
    mid = (s+e)//2
    if check(mid):
        ans = mid
        e = mid-1
    else:
        s = mid+1

print(ans)