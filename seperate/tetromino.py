import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_val = max(max(paper))

answer = 0
def solution(length, total, r, c):
    global answer
    # 더이상 진행해도 최댓값보다 커질 수 없는 경우
    if(total+max_val*(4-length)<=answer):
        return
    
    # 네칸째 방문일 경우
    if(length==4):
        answer = max(answer, total)
        return
    
    # 각 방향으로 탐색
    for d in direction:
        nr = r+d[0]
        nc = c+d[1]

        # 다음 방문할 칸이 존재하고 아직 방문한적이 없을 경우
        if ((0<=nr<n and 0<=nc<m) and not visited[nr][nc]):
            # 요철형태 처리
            if(length==2):
                visited[nr][nc] = True
                solution(length+1, total+paper[nr][nc], r, c)
                visited[nr][nc] = False
            visited[nr][nc] = True
            solution(length+1, total+paper[nr][nc], nr, nc)
            visited[nr][nc] = False
            
# 모든 칸을 기준으로 탐색실행
for r in range(n):
    for c in range(m):
        visited[r][c] = True
        solution(1, paper[r][c], r, c)
        visited[r][c] = False
print(answer)