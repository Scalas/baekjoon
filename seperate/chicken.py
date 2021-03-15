# 15686 치킨배달
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
vil = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []
answer = float('inf')
def solution(rm, idx):
    global answer
    # 필요한 수 만큼 폐업시켰을 경우
    if(rm==0):
        res = get_cval()
        answer = min(answer, res)
        return
    
    # 현재 폐업시킨 치킨집 이후의 치킨집들에 대해 재귀호출
    for i in range(idx+1,len(chicken)):
        removed[i] = True
        solution(rm-1, i)
        removed[i] = False
    
def get_cval():
    res = 0
    for i in range(len(house)):
        tmp = float('inf')
        for j in range(len(chicken)):
            if(not removed[j]):
                tmp = min(tmp, chicken_dist[i][j])
        res += tmp
    return res

# 집과 치킨집의 좌표정보 입력
for r in range(n):
    for c in range(n):
        if(vil[r][c]==1):
            house.append((r, c))
        elif(vil[r][c]==2):
            chicken.append((r, c))

chicken_dist = [[0 for _ in range(len(chicken))] for _ in range(len(house))]
removed = [False for _ in range(len(chicken))]

# 각 집과 치킨집간의 치킨거리 계산
for i in range(len(house)):
    for j in range(len(chicken)):
        chicken_dist[i][j] = abs(house[i][0]-chicken[j][0])+abs(house[i][1]-chicken[j][1])

remove = len(chicken)-m
if(remove > 0):
    for i in range(len(chicken)-remove+1):
        removed[i] = True
        solution(remove-1, i)
        removed[i] = False
else:
    answer = get_cval()

print(answer)