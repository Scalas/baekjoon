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

