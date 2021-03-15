# 13460 구슬탈출
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 11
red, blue = None, None
for r in range(n):
    for c in range(m):
        if (board[r][c] == 'R'):
            red = (r, c)
        if (board[r][c] == 'B'):
            blue = (r, c)


def solution(red, blue, d, count):
    global answer
    # 행동횟수를 1 늘리고 10을 넘어갈경우 종료
    count += 1
    if (count > 10):
        return

    # 두 구슬이 구멍에 빠지거나 움직일 수 없을때까지 이동
    red_moved, blue_moved, red_stop, blue_stop, red_inhole, blue_inhole = False, False, False, False, False, False
    while not (red_stop and blue_stop):
        red_r, red_c = red[0], red[1]
        blue_r, blue_c = blue[0], blue[1]
        if not (red_stop):
            red_r += d[0]
            red_c += d[1]
        if not (blue_stop):
            blue_r += d[0]
            blue_c += d[1]

        # 빨간구슬 이동
        if (not(red_stop) and (board[red_r][red_c] not in '#O') and not(red_r == blue_r and red_c == blue_c)):
            if((red_r == blue[0] and red_c == blue[1]) and (board[blue_r][blue_c] == '#')):
                red_stop = True
            else:
                red = (red_r, red_c)
                red_moved = True
        else:
            if (board[red_r][red_c] == 'O'):
                red_inhole = True
                red_moved = True
                red = (0, 0)
            red_stop = True

        # 파란구슬 이동
        if (not(blue_stop) and (board[blue_r][blue_c] not in '#O') and not(blue_r == red_r and blue_c == red_c)):
            if ((blue_r == red[0] and blue_c == red[1]) and (board[red_r][red_c] == '#')):
                blue_stop = True
            else:
                blue = (blue_r, blue_c)
                blue_moved = True
        else:
            if (board[blue_r][blue_c] == 'O'):
                blue_inhole = True
                blue_moved = True
                blue = (0, 0)
            blue_stop = True

    # 구슬이 전혀 움직이지 못했을경우
    if not(red_moved or blue_moved):
        return

    # 이동 종료 후 파란구슬이 구멍에 빠졌을 경우
    if (blue_inhole):
        return

    # 빨간구슬만 구멍에 빠졌을 경우
    if(red_inhole):
        answer = min(answer, count)
        return

    for i in range(4):
        if (direction[i] == d):
            continue
        solution(red, blue, direction[i], count)

for i in range(4):
    solution(red, blue, direction[i], 0)
if(answer==11):
    answer = -1
print(answer)