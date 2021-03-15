# 3109 빵집
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
land = [list(input().rstrip()) for _ in range(r)]
direction = (-1, 0, 1)
answer = 0
def solution(row, col):
    land[row][col] = 'x'
    # 끝까지 도달했을 경우 return True
    if(col == c-1):
        return True
    for i in range(3):
        nrow = row + direction[i]
        ncol = col + 1
        if(nrow<0 or nrow>=r or land[nrow][ncol]!='.'):
            continue
        if(solution(nrow, ncol)):
            return True
    return False
for i in range(r):
    if(solution(i, 0)):
        answer += 1
print(answer)