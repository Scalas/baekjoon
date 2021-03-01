import sys
input = sys.stdin.readline

''' 알고리즘 카테고리 : 그리드 '''
# 2839 설탕배달
def sol2839():
    n = int(input())
    pack5 = n//5
    remain = n%5
    answer = -1
    while remain<=n:
        if(remain%3 == 0):
            answer = pack5+(remain//3)
            break
        pack5 -= 1
        remain += 5
    print(answer)

# 11399 ATM
def sol11399():
    n = int(input())
    q = list(map(int, input().split()))
    q.sort()
    sum = 0
    answer = 0
    for time in q:
        if(time==0):
            continue
        sum += time
        answer += sum
    print(answer)

# 11047 동전0
def sol11047():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    answer = 0
    for coin in coins[::-1]:
        if(k==0):
            break
        answer += k//coin
        k %= coin
    print(answer)

# 1931 회의실 배정
def sol1931():
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    meetings.sort()
    answer = 0
    start_time = float('inf') 
    for meeting in meetings[::-1]:
        if(meeting[1]<=start_time):
            answer += 1
            start_time = meeting[0]
    print(answer)

# 5585 거스름돈
def sol5585():
    remain = 1000-int(input())
    coins = [500, 100, 50, 10, 5, 1]
    answer = 0
    for coin in coins:
        if(remain==0):
            break
        answer += remain//coin
        remain %= coin
    print(answer)

# 1541 잃어버린 괄호
def sol1541():
    oprd = [sum(map(int, oprd_sub.split('+'))) for oprd_sub in input().split('-')]
    print(oprd[0]-sum(oprd[1:]))

# 2217 로프
ROPE_MAX = 10000
def sol2217():
    n = int(input())
    ropes = [0]*(ROPE_MAX+1)
    for _ in range(n):
        ropes[int(input())] += 1

    answer = 0
    count = 0
    for i in range(ROPE_MAX, 0, -1):
        if(ropes[i]>0):
            count += ropes[i]
            answer = max(answer, count*i)
    print(answer)

# 1946 신입 사원
def sol1946():
    case = int(input())
    answers = []
    for _ in range(case):
        n = int(input())
        scores = [0]*(n+1)
        for _ in range(n):
            s1, s2 = map(int, input().split())
            scores[s1] = s2
        answer = 1
        min = scores[1]
        for score in scores[2:]:
            if(score<min):
                answer += 1
                min = score
        answers.append(str(answer))
    print('\n'.join(answers))

# 1339 단어 수학
def sol1339():
    n = int(input())
    alpha_weight = [0]*26
    digits = list(range(10))
    for _ in range(n):
        word = input().rstrip()
        digit = len(word)
        for c in word:
            alpha_weight[ord(c)-ord('A')] += (10**(digit-1))
            digit -= 1
    alpha_weight.sort(reverse=True)
    answer = 0
    for weight in alpha_weight:
        if(weight==0):
            break
        answer += weight*digits.pop()
    print(answer)

# 4796 캠핑
def sol4796():
    answers = []
    case_num = 1
    while True:
        l, p, v = map(int, input().split())
        if(l==p==v==0):
            break
        answer = (v//p)*l
        v %= p
        answer += min(v, l)
        answers.append(f'Case {case_num}: {answer}')
        case_num += 1
    print('\n'.join(answers))