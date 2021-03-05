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

# 1080 행렬
def sol1080():
    n, m = map(int, input().split())
    count = 0

    # 기존 행렬 mat1과 만들려는 행렬 mat2
    mat1 = [list(map(int, input().rstrip())) for _ in range(n)]
    mat2 = [list(map(int, input().rstrip())) for _ in range(n)]

    # mat1과 mat2의 값이 다를 경우 
    # 그 점을 기준점으로 3*3크기의 부분행렬에 대해 변환연산을 실행
    # 3*3크기의 부분행렬이 나오지않아 연산이 불가능한경우 반복문 탈출
    try:
        for i in range(n):
            for j in range(m):
                if(mat1[i][j] != mat2[i][j]):
                    mat_rev(mat1, i, j, n, m)
                    count+=1
    except:
        None
    
    # 반복분 실행결과 mat1이 mat2와 같아진 경우
    if(mat1==mat2):
        print(count)
    # 같아지지 못한 경우
    else:
        print(-1)

# 행렬 변환연산
def mat_rev(mat, st_i, st_j, n, m):
    if((st_i+2<n) and (st_j+2<m)):
        for i in range(3):
            for j in range(3):
                mat[st_i+i][st_j+j] = int(bool(mat[st_i+i][st_j+j]) == False)
        return True
    else:
        return False

# 1744 수 묶기
def sol1744():
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    seq.sort()
    answer = 0
    while(len(seq) > 1):
        num1 = seq.pop()
        if(num1<=0):
            seq.append(num1)
            break
        num2 = seq.pop()
        if(num2<=0):
            answer += num1
            seq.append(num2)
            break

        if(num1>1 and num2>1):
            answer += num1*num2
        else:
            answer += num1+num2
    
    for i in range(0, len(seq), 2):
        num1 = seq[i]
        if(i<len(seq)-1):
            num2 = seq[i+1]
            answer += num1*num2
        else:
            answer += num1
    print(answer)

# 1715 카드 정렬하기
import heapq
def sol1715():
    n = int(input())
    q = []
    for _ in range(n):
        heapq.heappush(q, int(input()))
    
    answer = 0
    while(len(q)>1):
        sum = heapq.heappop(q)+heapq.heappop(q)
        answer += sum
        heapq.heappush(q, sum)

    print(answer)

# 2437 저울
def sol2437():
    n = int(input())
    weights = list(map(int, input().split()))
    weights.sort()

    if(weights[0]>1):
        print(1)
    else:
        weight_sum = 0
        for i in range(n):
            weight_sum += weights[i]
            if(i == n-1):
                print(weight_sum + 1)
                break
            if(weights[i+1]-weight_sum > 1):
                print(weight_sum+1)
                break

# 1783 병든 나이트
import math
def sol1783():
    n, m = map(int, input().split())
    if(n == 1):
        print(1)
    elif(n == 2):
        print(min(math.ceil(m/2), 4))
    else:
        if(m<7):
            print(min(m, 4))
        else:
            print(m-2)

# 1449 수리공 항승
def sol1449():
    n, l = map(int, input().split())
    pipe = [1 for _ in range(1000)]
    for num in input().split():
        pipe[int(num)-1] = 0
    
    count = 0
    pass_count = 0
    for i in range(1000):
        if(pass_count>0):
            pass_count -= 1
            continue
        if(pipe[i] == 0):
            pass_count = 2
            count += 1    
    print(count)

# 1202 보석도둑
def sol1202():
    n, k = map(int, input().split())
    q = []
    gems = [tuple(map(int, input().split())) for _ in range(n)] 
    bags = [int(input()) for _ in range(k)]

    gems.sort(reverse=True)
    bags.sort()
    answer = 0

    for bag in bags:
        while(gems and gems[-1][0]<=bag):
            heapq.heappush(q, -gems.pop()[1])
        if(q):
            answer += (-heapq.heappop(q))
    print(answer)
    
# 1439 뒤집기
def sol1439():
    s_list = input().rstrip().split('1')
    cont_zero = len(s_list) - s_list.count('')
    cont_one = cont_zero - 1
    if s_list[0]=='':
        cont_one += 1
    if s_list[len(s_list)-1]=='':
        cont_one += 1
    print(min(cont_zero, cont_one))

# 2847 게임을 만든 동준이
def sol2847():
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    answer = 0
    for i in range(n-2,-1,-1):
        if(scores[i] >= scores[i+1]):
            count = scores[i]-scores[i+1]+1
            scores[i] -= count
            answer += count
    print(answer)

# 1700 멀티탭 스케줄링
def sol1700():
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    using = []
    answer = 0
    for i in range(k):
        cur = q[i]
        if(cur in using):
            continue
        else:
            if(len(using) < n):
                using.append(cur)
            else:
                next_use = 0
                target = 0
                for num in using:
                    if(num not in q[i+1:]):
                        target = num
                        break
                    use_seq = q[i+1:].index(num)
                    if(i+1+use_seq > next_use):
                        next_use = i+1+use_seq
                        target = num
                using.remove(target)
                using.append(cur)
                answer += 1
    print(answer)

