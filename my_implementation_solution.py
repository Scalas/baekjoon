import sys
import math
input = sys.stdin.readline

''' 알고리즘 카테고리 : 구현 '''


# 11721 열 개씩 끊어 출력하기
def sol11721():
    word = input()
    for i in range(0, len(word), 10):
        print(word[i:i+10])

# 2446 별찍기9
def sol2446():
    n = int(input())
    result = []
    for i in range(-n+1, n):
        result.append(' '*(n-abs(i)-1)+'*'*(2*abs(i)+1))
    print('\n'.join(result))

# 2442 별찍기5
def sol2442():
    n = int(input())
    result = []
    for i in range(n):
        result.append(' '*(n-1-i)+'*'*(2*i+1))
    print('\n'.join(result))

# 2747 피보나치 수
def sol2747():
    n = int(input())
    fibo = [0, 1]
    if(n<2):
        print(fibo[n])
    else:
        for i in range(2,n+1):
            fibo.append(fibo[-1]+fibo[-2])
        print(fibo[-1])

# 2523 별찍기13
def sol2523():
    n = int(input())
    result = []
    for i in range(-n+1, n):
        result.append('*'*(n-abs(i)))
    print('\n'.join(result))

# 2445 별찍기8
def sol2445():
    n = int(input())
    result = []
    for i in range(-n+1, n):
        result.append('*'*(n-abs(i))+' '*(2*abs(i))+'*'*(n-abs(i)))
    print('\n'.join(result))

# 2444 별찍기7
def sol2444():
    n = int(input())
    result = []
    for i in range(-n+1, n):
        result.append(' '*abs(i)+'*'*(2*(n-abs(i))-1))
    print('\n'.join(result))

# 1966 프린터큐
def sol1966():
    t = int(input())
    answer = []
    for i in range(t):
        n, m = map(int, input().split())
        q = list(map(int, input().split()))
        idx = 0
        print_count = 0
        while(q):
            if(q[0]==max(q)):
                del q[0]
                print_count += 1
                if(idx == m):
                    answer.append(str(print_count))
                    break
            else:
                q.append(q[0])
                del q[0]
                if(idx == m):
                    m += len(q)
            idx += 1
    print('\n'.join(answer))

# 10773 제로
def sol10773():
    k = int(input())
    nums = []
    for i in range(k):
        num = int(input())
        if(num!=0):
            nums.append(num)
        else:
            nums.pop()
    print(sum(nums))

# 2443 별찍기6
def sol2443():
    n = int(input())
    result = []
    for i in range(n):
        result.append(' '*i+'*'*(2*(n-i)-1))
    print('\n'.join(result))

# 2475 검증수
def sol2475():
    sum = 0
    for num in map(int, input().split()):
        sum+=(num**2)
    print(sum%10)

# 1475 방 번호
def sol1475():
    num = int(input())
    if(num == 0):
        print(1)
        return
    count = [0]*10
    while(num>0):
        count[num%10] += 1
        num //= 10
    count[6] = int(math.ceil((count[6]+count[9])/2))
    count[9] = 0
    print(max(count))

# 2490 윷놀이
def sol2490():
    res = ['E', 'A', 'B', 'C', 'D']
    answer = []
    for _ in range(3):
        back = list(map(int, input().split())).count(0)
        answer.append(res[back])
    print('\n'.join(answer))

# 11050 이항계수
def sol11050():
    n, k = map(int, input().split())
    top, bot = 1, 1
    for num in range(1, k+1):
        top *= (n-num+1)
        bot *= num
    print(top//bot)

# 2455 지능형 기차
def sol2455():
    nums = []
    for i in range(4):
        pout, pin = map(int, input().split())
        num = pin-pout
        if(i>0):
            num += nums[i-1]
        nums.append(num)
    print(max(nums))

# 1476 날짜 계산
def sol1476():
    e, s, m = map(int, input().split())
    if(e==15):
        e = 0
    if(s==28):
        s = 0
    if(m==19):
        m = 0
    answer = s
    while True:
        if(answer%15==e and answer%28==s and answer%19==m):
            break
        answer += 28
    print(answer)

# 3009 네 번째 점
def sol3009():
    xval = []
    yval = []
    for _ in range(3):
        x, y = map(int, input().split())
        if x in xval:
            xval.remove(x)
        else:
            xval.append(x)
        if y in yval:
            yval.remove(y)
        else:
            yval.append(y)
    print(xval[0], yval[0])

# 3046 R2
def sol3046():
    r1, s = map(int, input().split())
    print(2*s-r1)

# 10808 알파벳 개수
def sol10808():
    s = input().rstrip()
    answer = [0 for _ in range(26)]
    for c in s:
        answer[ord(c)-ord('a')] += 1
    print(' '.join(map(str, answer)))

# 2743 단어 길이재기
def sol2743():
    print(len(input().rstrip()))

# 14503 로봇청소기
def sol14503():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    floor = [list(map(int, input().split())) for _ in range(n)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    answer = 0
    while True:
        # 현재위치를 청소
        if(floor[r][c] == 0):
            floor[r][c] = 2
            answer += 1
        
        # 왼쪽부터 네 방향을 탐색
        sc = 0
        while(sc<4):
            tr = r+direction[d-1][0]
            tc = c+direction[d-1][1]
            # 왼쪽방향에 청소할 공간이 없다면
            if(floor[tr][tc]==1 or floor[tr][tc] == 2):
                sc += 1
                d -= 1
                if(d==-1):
                    d = 3
                continue
                
            # 왼쪽방향에 청소할 공간이 있다면
            r = tr
            c = tc
            d -= 1
            if(d==-1):
                d = 3
            break
            
        # 사방에 청소할 공간이 없을 경우
        if(sc==4):
            tr = r-direction[d][0]
            tc = c-direction[d][1]
            # 후진할 공간이 없다면 작동정지
            if(floor[tr][tc]==1):
                break
            
            # 후진할 수 있다면 방향을 유지하고 후진
            r = tr
            c = tc
            continue
    print(answer)

# 10996 별찍기21
def sol10996():
    n = int(input())
    res = []
    for i in range(n*2):
        for j in range(n):
            if((i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)):
                res.append('*')
            else:
                res.append(' ')
        res.append('\n')
    print(''.join(res))

# 2108 통계학
def sol2108():
    n = int(input())
    nums = [0]*8001
    sum_val, med, min_val, max_val, mode = 0, 0, 4001, -4001, 0
    answer = []
    for i in range(n):
        num = int(input())
        nums[num+4000] += 1
        sum_val += num
    answer.append(str(round(sum_val/n)))

    idx = 0
    max_count = max(nums)
    mode_count = 0
    for i in range(8001):
        if(nums[i]==0):
            continue
        if(idx==0):
            min_val = i-4000
        max_val = i-4000
        if(nums[i]==max_count and mode_count<2):
            mode = i-4000
            mode_count += 1
        while(nums[i]>0):
            nums[i] -= 1
            idx += 1
            if(idx == (n+1)//2):
                med = i-4000

    answer.append(str(med))
    answer.append(str(mode))
    answer.append(str(max_val-min_val))
    print('\n'.join(answer))

# 2522 별찍기12
def sol2522():
    n = int(input())
    answer = []
    for i in range(-n+1, n):
        answer.append(' '*abs(i)+'*'*(n-abs(i)))
    print('\n'.join(answer))

# 3190 뱀
from collections import deque
def solution():
    n = int(input())
    k = int(input())
    apple = [tuple(map(int, input().split())) for _ in range(k)]
    l = int(input())
    cmd = []
    for _ in range(l):
        inp = input().split()
        cmd.append((int(inp[0]), inp[1]))
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    time = 0
    snake = deque([(1, 1)])
    d = 1
    ridx = 0
    while True:
        time += 1
        # 몸길이를 늘려 머리를 다음칸에 위치
        new_head = (snake[-1][0]+direction[d][0], snake[-1][1]+direction[d][1])
        
        # 다음 머리가 이동할 칸이 벽이거나 자신의 몸이 위치한 곳일 경우 종료
        if not(1<=new_head[0]<=n and 1<=new_head[1]<=n) or (new_head in snake):
            break
            
        # 이동할 수 있다면 머리를 다음칸에 위치
        snake.append(new_head)
        
        # 사과가 있다면 사과를 먹고 몸길이가 그대로
        if(new_head in apple):
            apple.remove(new_head)
        # 사과가 없다면 꼬리를 없앤다
        else:
            snake.popleft()
        
        # 방향전환
        if(ridx<l and time == cmd[ridx][0]):
            if(cmd[ridx][1]=='D'):
                d += 1
                if(d==4):
                    d = 0
            else:
                d -= 1
                if(d==-1):
                    d = 3
            ridx += 1
    print(time)

# 1100 하얀칸
def sol1100():
    board = [input().rstrip() for _ in range(8)]
    answer = 0
    for i in range(8):
        for j in range(8):
            if(board[i][j]=='F'):
                if(i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    answer+=1
    print(answer)

# 1009 분산처리
def sol1009():
    t = int(input())
    answers = []
    for i in range(t):
        a, b = map(int, input().split())
        answer = (power(a, b))
        if(answer == 0):
            answer = 10
        answers.append(str(answer))
    print('\n'.join(answers))
def power(a, b):
    if(b==0):
        return 1
    res = (power(a, b//2)**2)%10
    if(b%2!=0):
        res *= a
        res %= 10
    return res%10

# 1009 분산처리 다른풀이
def sol1009_2():
    t = int(input())
    answers = []
    for i in range(t):
        a, b = map(int, input().split())
        a %= 10
        b = b%4+4
        answer = a**b
        if(answer == 10):
            answer = 10
        answers.append(str(answer))
    print('\n'.join(answers))

# 10797 10부제
def sol10797():
    day = input().rstrip()
    print(input().rstrip().count(day))

# 14499 주사위 굴리기
def sol14499():
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cmd_list = list(map(int, input().split()))
    dice = {'top':0, 'bottom':0, 'front':0, 'back':0, 'left':0, 'right':0}
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    answer = []
    for cmd in cmd_list:
        nx, ny = x+d[cmd-1][0], y+d[cmd-1][1]
        if not(0<=nx<n and 0<=ny<m):
            continue
        x, y = nx, ny
        if(cmd==1):
            dice['bottom'], dice['left'], dice['top'], dice['right'] = dice['right'], dice['bottom'], dice['left'], dice['top']
        elif(cmd==2):
            dice['bottom'], dice['left'], dice['top'], dice['right'] = dice['left'], dice['top'], dice['right'], dice['bottom']
        elif(cmd==3):
            dice['bottom'], dice['front'], dice['top'], dice['back'] = dice['front'], dice['top'], dice['back'], dice['bottom']
        elif(cmd==4):
            dice['bottom'], dice['front'], dice['top'], dice['back'] = dice['back'], dice['bottom'], dice['front'], dice['top']
        if(board[x][y]==0):
            board[x][y] = dice['bottom']
        else:
            dice['bottom'] = board[nx][ny]
            board[x][y] = 0
        answer.append(str(dice['top']))
    print('\n'.join(answer))

# 1032 명령프롬프트
def sol1032():
    n = int(input())
    files = [input().rstrip() for _ in range(n)]
    answer = list(files[0])
    name_len = len(files[0])
    for file in files[1:]:
        for i in range(name_len):
            if(answer[i] != file[i]):
                answer[i] = '?'
    print(''.join(answer))

# 5338 마이크로소프트 로고
def sol5338():
    res = []
    res.append('       _.-;;-._')
    res.append('\'-..-\'|   ||   |')
    res.append('\'-..-\'|_.-;;-._|')
    res.append('\'-..-\'|   ||   |')
    res.append('\'-..-\'|_.-\'\'-._|')
    print('\n'.join(res))