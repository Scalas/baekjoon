import sys
import heapq
from collections import deque

input = sys.stdin.readline
out = sys.stdout.write


#1026 보물
def sol1026():
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_a.sort()
    arr_b = list(map(int, input().split()))
    arr_b.sort(reverse=True)
    
    answer = 0
    for i in range(n):
        answer += (arr_a[i]*arr_b[i])
    
    print(answer)


#10815 숫자카드
def sol10815():
    n = int(input())
    cards = set(map(int, input().split()))
        
    m = int(input())
    answer = []
    for num in map(int, input().split()):
        if(num in cards):
            answer.append('1')
        else:
            answer.append('0')
    print(' '.join(answer))


#1764 듣보잡
def sol1764():
    n, m = map(int, input().split())
    l = set([input().rstrip() for _ in range(n)])
    s = set([input().rstrip() for _ in range(m)])
    answer = sorted(list(l&s))
    
    print(len(answer))
    print('\n'.join(answer))


#10610 30
# 모든 자릿수의 합이 3의 배수이면 
# 그 숫자는 3의 배수라는 점을 활용해야함
def sol10610_2():
    n = list(input().rstrip())
    n.sort(reverse=True)
    # 30의 배수이려면 끝자리가 0이며 
    # 남머지 자릿수의 합이 3의 배수여야한다
    if(n[-1]=='0' and sum(map(int, n))):
        print(''.join(n))
    else:
        print(-1)


#10825 국영수
# 첫 풀이는 단순히 람다식을 이용한 정렬
def sol10825():
    n = int(input())
    datas = []
    for _ in range(n):
        data = input().split()
        datas.append((data[0], int(data[1]), int(data[2]), int(data[3])))
    datas.sort(key=lambda x:(-x[1], x[2], x[3], x[0]))
    for data in datas:
        out(data[0]+'\n')

# 정렬 결과로 이름만 출력하면 되기 때문에
# 정렬기준으로만 사용될 점수들은 변형을 가해도 된다
# 감소순서로 정렬해야할 국어점수와 수학점수에 
# 마이너스를 취하고 우선순위 순서대로 저장하여 정렬하면 
# 람다식의 사용 없이 sort()만으로 원하는대로 정렬된다.
# 람다식을 사용한 정렬보다 빠른 속도를 보인다
def sol10825_2():
    n = int(input())
    datas = []
    for _ in range(n):
        data = input().split()
        datas.append((-int(data[1]), int(data[2]), -int(data[3]), data[0]))
    datas.sort()
    for data in datas:
        out(data[-1]+'\n')


#11656 접미사배열
def sol11656():
    s = input().rstrip()
    print('\n'.join(sorted([s[i:] for i in range(len(s))])))


#11728 배열합치기
def sol11728():
    n, m = map(int, sys.stdin.readline().split())
    arr = sorted(list(map(int, sys.stdin.read().split())))
    print(' '.join(map(str, arr)))


#5052 전화번호 목록
def sol5052():
    t = int(input())
    for _ in range(t):
        n = int(input())
        pns = sorted([input().rstrip() for _ in range(n)])
        
        res = True
        for i in range(n-1):
            if(pns[i+1].startswith(pns[i])):
                res = False
                break
        if(res):
            print('YES')
        else:
            print('NO')


#2822 점수계산
def sol2822():
    res = sorted([(int(input()), i+1) for i in range(8)])[-5:]
    
    total = 0
    pnum = []
    for r in res:
        total += r[0]
        pnum.append(r[1])
    pnum.sort()
    
    print(total)
    print(' '.join(map(str, pnum)))


#11652 카드
def sol11652():
    n = int(input())
    cards = {}
    for _ in range(n):
        num = int(input())
        try:
            cards[num] += 1
        except:
            cards[num] = 1
    counts = sorted(list(zip(cards.keys(), cards.values())), key=lambda x:(-x[1], x[0]))
    print(counts[0][0])


#7453 합이 0인 네 정수
# 나중에 다시풀어볼것
# 첫 풀이는 결국 힌트를 보고 dictionary를 활용하여 풀음
# 실행 시간은 상위권 풀이의 두배가량
# 네 수의 합을 두 수의 합끼리의 합으로 보고
# 두 수의 합이 서로 부호만 다른 경우의 수를
# 찾는 방향으로 접근해야함
def sol7453():
    n = int(input())
    A = []
    B = []
    C = []
    D = []
    sum_ab = []
    sum_cd = {}
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    
    for i in range(n):
        for j in range(n):
            sum_ab.append(A[i]+B[j])
            try:
                sum_cd[C[i]+D[j]] += 1
            except:
                sum_cd[C[i]+D[j]] = 1
    
    answer = 0
    for ab in sum_ab:
        try:
            cd_count = sum_cd[-ab]
            answer += cd_count
        except:
            continue
    print(answer)


# 가장 좋은 풀이는 두 수의 합을 각각 오름차순, 내림차순 정렬하여
# 두 수의 합이 0보다 크면 내림차순 정렬한 합 배열의 다음 요소를
# 두 수의 합이 0보다 작으면 오름차순 정렬한 합배열의 다음 요소를 참조하여
# 0인 조합을 찾을경우 
# 그 조합과 같은 순서쌍을 모두 찾아 그 수를 합산하는 방식이다.


#1302 베스트셀러
# 딕셔너리에 책이름을 key로, 팔린 수를 value로 저장 후 
# 키/값 쌍을 값기준 내림차순, 값이 같을경우 키(이름)기준 오름차순 정렬하여 첫번째 요소의 책이름을 출력
def sol1302():
    n = int(input())
    sold = {}
    for _ in range(n):
        book = input().rstrip()
        try:
            sold[book] += 1
        except:
            sold[book] = 1
    
    rank = sorted(list(sold.items()), key=lambda x:(-x[1], x[0]))
    print(rank[0][0])


#8979 올림픽
def sol8979():
    n, k = map(int, input().split())

    # 국가의 메달 정보를 국가번호:메달정보 쌍으로 저장
    nations = {}
    for _ in range(n):
        nation = tuple(map(int, input().split()))
        nations[nation[0]] = nation[1:]

    # 메달 정보를 기준에따라 정렬
    rank = sorted(nations.values(), key=lambda x: (-x[0], -x[1], -x[2]))
    
    # 해당 국가보다 성적이 좋은 국가의 수 + 1이므로 초기값은 1
    # 등수를 구하려는 국가와 같은 성적이 나오기 전까지 등수 +1
    answer = 1
    for r in rank:
        if(r==nations[k]):
            break
        answer += 1

    print(answer)


#10867 중복빼고 정렬하기
# 입력받은 데이터를 집합으로 변환한 뒤 다시 리스트로 변환하여 정렬
def sol10867():
    input()
    print(*sorted(list(set(map(int, input().split())))))


#2075 n번째 큰수
def sol2075():
    n = int(input())
    nums = []
    for i in range(n):
        for num in map(int, input().split()):
            if(len(nums)<n):
                heapq.heappush(nums, -num)
            elif(nums[-1]>-num):
                heapq.heappop(nums)
                heapq.heappush(nums, -num)
            print(nums)
                
    print(-nums[0])



# 못푼문제
# 2887 행성터널 - 최소비용신장트리
# 1517 버블소트 - 머지정렬을 활용한 inversion count


#11557 Yangjojang of The Year
def sol11557():
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())
        s = [input().split() for _ in range(n)]
        s.sort(key=lambda x:int(x[1]))
        answers.append(s[-1][0])
    print('\n'.join(answers))


#18870 좌표 압축
def sol18870():
    n = int(input())
    p = list(map(int, input().split()))
    s = sorted(list(set(p)))
    
    z = {}
    for i, num in enumerate(s):
        z[num] = i
    
    out(' '.join(map(str, [z[num] for num in p])))


#5576 콘테스트
def sol5576():
    w = sum(sorted([int(input()) for _ in range(10)])[-3:])
    k = sum(sorted([int(input()) for _ in range(10)])[-3:]) 
    out(' '.join(map(str, (w, k))))


#1015 수열 정렬
def sol1015():
    n = int(input())
    a = list(map(int, input().split()))
    
    p = {}
    for i, num in enumerate(sorted(a)):
        if(p.get(num)==None):
            p[num] = deque([i])
        else:
            p[num].append(i)
        
    answer = []
    for num in a:
        answer.append(p[num].popleft())
        
    print(' '.join(map(str, answer)))


#11931 수 정렬하기4
def sol11931():
    n = int(input())
    out('\n'.join(map(str, sorted([int(input()) for _ in range(n)], reverse=True))))


#2693 n번째 큰 수
def sol2693():
    case = [list(map(int, input().split())) for _ in range(int(input()))]
    print('\n'.join(map(str, [sorted(c)[-3] for c in case])))


#1431 시리얼 번호
def ds(str):
    return sum([int(c) for c in str if c.isdigit()])
            

def sol1431():
    sn = [input().rstrip() for _ in range(int(input()))]
    sn.sort(key= lambda x:(len(x), ds(x), x))
    print('\n'.join(sn))


#11000 강의실배정
# 강의를 시작시간 순으로
# 시작시간이 같으면 종료시간 순으로 오름차순 정렬
# 빈 강의실이 없을 때 시작되는 수업의 갯수를 찾는다
def sol11000():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l.sort()
    
    # 처음엔 강의종료시간 el을 전부 탐색해서 시간초과
    # heapq를 사용해서 가장 빨리 강의가 끝나는 강의실 탐색
    answer = 0
    el = []
    for s, t in l:
        # 시작전에 비는 강의실이 없는경우 강의실+1
        if(not el or el[0]>s):
            answer += 1
            heapq.heappush(el, t)

        # 있을경우 가장 빨리 비는 강의실에서 강의시작
        else:
            heapq.heappop(el)
            heapq.heappush(el, t)

    out(str(answer))


#2776 암기왕
def sol2776():
    for _ in range(int(input())):
        input()
        nums = set(map(int, input().split()))
        input()
        q = list(map(int, input().split()))
        out('\n'.join([('1' if num in nums else '0') for num in q])+'\n')


#3273 두 수의 합
# 정렬 후 작은 수부터 x의 보수가 존재하는지 확인
# x의 보수가 자신보다 큰 수라면 answer += 1
# 그렇지 않다면 break

# 여기서는 보수의 존재를 확인하기 위해 set을 사용
# 수의 범위가 1에서 100만 사이로 크지 않기때문에
# 카운팅 정렬도 사용 가능
def sol3273():
    input()
    arr = list(map(int, input().split()))
    x = int(input())
    arr.sort()
    
    answer = 0
    s = set(arr)
    for num in arr:
        if (x-num) in s:
            if(num<x-num):
                answer += 1
            else:
                break
    out(str(answer))


#2170 선긋기
# x y 쌍을 오름차순 정렬
# 겹치는것들을 겹쳐나감
# 겹치지 않는 선이 생겼을 경우 기존의 선의 길이를 더한 뒤 시작점과 끝점을 재설정

# 1. 단순히 리스트형태로 저장하여 정렬해도 해결가능

# 2. 시작점:끝점의 키값 쌍으로 매핑한 뒤
# 키 값만을 정렬하여 해결 가능하다
# 정렬 대상이 튜플이 아닌 정수형이며
# 같은 시작점을 가진 데이터가 하나로 합쳐지기 떄문에
# 정렬 시간을 대폭 줄일 수 있다.
def sol2170():
    n = int(input())
    lines = {}
    for _ in range(n):
        x, y = map(int, input().split())
        try:
            lines[x] = max(lines[x], y)
        except:
            lines[x] = y

    l = sorted(lines.keys())
    answer = 0
    s = l[0]
    e = lines[l[0]]
    for x in l[1:]:
        y = lines[x]
        if(x > e):
            answer += e-s
            s = x
        e = max(e, y)
    answer += e-s
    out(str(answer))


#5635 생일
def sol5635():
    n = int(input())
    stdt = [input().split() for _ in range(n)]
    stdt = sorted(stdt, key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
    out('\n'.join((stdt[-1][0], stdt[0][0])))


#8983 사냥꾼
# 각 동물마다 동물을 잡을 수 있는 사대를 탐색
# 동물 최대수 N, 사대 최대수 M일 때
# O(NlogM)의 성능
def search(pos, target, l):
    left = 0
    right = len(pos)-1
    while(left<=right):
        m = (left+right)//2
        if(target[1]-l <= pos[m]-target[0] <= l-target[1]):
            return True
        elif(pos[m]<target[0]):
            left = m+1
        else:
            right = m-1
    return False


def sol8983():
    m, n, l = map(int, input().split())
    pos = sorted(list(map(int, input().split())))
    target = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x:x[1])
    
    answer = 0
    for t in target:
        if(t[1]>l):
            continue
        if(search(pos, t, l)):
            answer += 1
    print(answer)


#1377 버블 소트
# 각 숫자의 정렬 이후의 위치가 
# 기존 위치보다 뒤일 경우 1번의 순회가 필요
# 기존 위치보다 전일 경우 기존 위치와의 차이만큼의 순회가 필요
# 각 숫자가 제 위치로 가기 위해 필요한 순회 횟수중
# 가장 큰 것을 찾는다
def sol1377():
    n = int(input())
    arr = sorted([(int(input()), i) for i in range(n)])
    
    answer = 0
    for i in range(n):
        move = arr[i][1]-i
        if(move<0):
            move = 1
        answer = max(answer, move)
    print(answer+1)


#2467 용액
# 투포인터 응용문제
# 수치를 정렬한 뒤
# 좌측과 우측에서 값을 가져와 합을 구함
def sol2467():
    n = int(input())
    lq = sorted(map(int, input().split()))
    s = 0
    e = n-1
    sum_val = 2000000000
    a, b = 0, 0
    while s<e:
        su = lq[s]+lq[e]
        if(abs(su) < abs(sum_val)):
            sum_val = su
            a, b = lq[s], lq[e]
        if(su<0):
            s += 1
        elif(su>0):
            e -= 1
        else:
            break
            
    print(*sorted([a, b]))


#2473 세 용액
# 투포인터 응용문제
# 수치 하나를 고른 뒤
# 나머지 수치들중 두 수를 투포인터로 탐색
# 합이 가장 작은 절댓값을 가지는 쌍을 구함
# 합이 0일경우 탐색을 종료하고 바로 답을 출력
def sol2473():
    n = int(input())
    lq = sorted(map(int, input().split()))
    
    answer = [[0, 0, 0], float('inf')]
    for m in range(n-2):
        a = lq[m]
        s = m+1
        e = n-1
        check = False
        while(s<e):
            b, c = lq[s], lq[e]
            su = a+b+c
            if(abs(su)<answer[1]):
                answer[1] = abs(su)
                answer[0][0], answer[0][1], answer[0][2] = a, b, c
            if(su<0):
                s += 1
            elif(su>0):
                e -= 1
            else:
                check = True
                break
        if(check):
            break
                
    print(*sorted(answer[0]))


#11497 통나무 건너뛰기
# 맨 앞과 맨 뒤의 값의 차이도 포함하여
# 난이도를 최소화 해야함
# 정렬의 방식을 조금 바꿔야함
# 1 2 3 4 5  =>  1 3 5 4 2
def sol11497():
    for _ in range(int(input())):
        n = int(input())
        wood = sorted(map(int, input().split()))
        arr = deque()
        s = True
        for w in wood:
            if(s):
                arr.appendleft(w)
                s = not s
            else:
                arr.append(w)
                s = not s
                
        level = 0
        for i in range(n):
            level = max(level, abs(arr[i]-arr[i-1]))
        print(level)


#1940 주몽
# 더해서 특정 값이 되는 값의 쌍 탐색
# 투포인터 활용문제
def sol1940():
    n = int(input())
    m = int(input())
    material = list(map(int, input().split()))
    material.sort()
    
    s, e = 0, n-1
    answer = 0
    while(s<e):
        val = material[s]+material[e]
        if(val== m):
            answer += 1
            s += 1
            e -= 1
        elif(val<m):
            s += 1
        else:
            e -= 1
    print(answer)


#2212 센서
# 직선상의 좌표들을 정해진 갯수의 집중국으로 연결
# 집중국의 수신범위의 합을 최소화
# 집중국 갯수-1 만큼 좌표 사이를 끊어내는 방식으로 접근
def sol2212():
    n = int(input())
    k = int(input())

    if (n <= k):
        print(0)
    else:
        sensors = sorted((map(int, input().split())))
        answer = sensors[-1] - sensors[0]
        links = [sensors[i+1]-sensors[i] for i in range(n - 1)]
        links.sort()
        for _ in range(k - 1):
            answer -= links.pop()

        print(answer)


#2628 종이자르기
# 가로 세로의 잘라진 길이들을 정렬
# 가로 세로의 가장 큰 길이끼리 곱한 값
def sol2628():
    n, m = map(int, input().split())
    k = int(input())

    cuts = [[0], [0]]
    for _ in range(k):
        t, p = map(int, input().split())
        cuts[t].append(p)
    cuts[0].append(m)
    cuts[1].append(n)
    cuts[0].sort()
    cuts[1].sort()

    w = []
    for i in range(1, len(cuts[0])):
        w.append(cuts[0][i] - cuts[0][i - 1])

    h = []
    for i in range(1, len(cuts[1])):
        h.append(cuts[1][i] - cuts[1][i - 1])

    print(max(w) * max(h))


#5800 성적 통계
# 각 학급의 최대점수, 최소점수, 최대 인접점수간 차이를 각각 구함
def sol5800():
    k = int(input())
    classes = [list(map(int, input().split()))[1:] for _ in range(k)]
    answer = []
    for idx, c in enumerate(classes):
        c.sort()
        gap = 0
        for i in range(1, len(c)):
            gap = max(gap, c[i]-c[i-1])
        answer.append(f'Class {idx+1}')
        answer.append(f'Max {c[-1]}, Min {c[0]}, Largest gap {gap}')
    print('\n'.join(answer))


#10800 컬러볼
# 자신보다 작은 크기의 다른색깔 공만 잡을 수 있는 게임
def sol10800():
    n = int(input())
    balls = [(i, *map(int, input().split())) for i in range(n)]
    # 크기순, 색깔 순으로 정렬
    balls.sort(key=lambda x: (x[2], x[1]))

    # 모든 공의 크기의 합과 색깔별 크기의 합을 갱신
    answer = [0] * n
    ball_sum = 0
    c_sums = [0] * n
    pre = 0
    for i, ball in enumerate(balls):
        # 크기가 같은 공끼리 영향을 주지 않도록
        # 같은 크기의 공들의 정보는 한번에 갱신
        while (balls[pre][2] < ball[2]):
            ball_sum += balls[pre][2]
            c_sums[balls[pre][1] - 1] += balls[pre][2]
            pre += 1
        # 자신과 같은색의 공의 크기의 합을 전체의 합에서 뺀다
        answer[ball[0]] = ball_sum - c_sums[ball[1] - 1]
    print(*answer)


#6996 애너그램
# 정렬한 뒤 비교연산
def sol6996():
    answer = []
    for _ in range(int(input())):
        str1, str2 = input().split()
        if (len(str1) != len(str2)):
            answer.append(f'{str1} & {str2} are NOT anagrams.')
            continue
        s1 = [0] * 26
        s2 = [0] * 26
        for i in range(len(str1)):
            s1[ord(str1[i]) - ord('a')] += 1
            s2[ord(str2[i]) - ord('a')] += 1
        if (s1 == s2):
            answer.append(f'{str1} & {str2} are anagrams.')
        else:
            answer.append(f'{str1} & {str2} are NOT anagrams.')
    print('\n'.join(answer))


#8980 택배
# 단방향으로 운행하는 트럭이 나를 수 있는 최대 박스 수 
# 보내는 마을, 받는 마을 순으로 정렬
# 적재할 자리가 부족할 때 단순히 남는 자리만큼 넣는것으로 처리하여 틀림
# 넣으려는 박스보다 도착마을이 먼 박스를 버려야 정답
# 트럭이 싣고있는 박스를 도착 위치별로 관리
def sol8980():
    n, c = map(int, input().split())
    boxes = {}
    for _ in range(int(input())):
        s, e, num = map(int, input().split())
        try:
            boxes[s].append((e, num))
        except:
            boxes[s] = [(e, num)]

    t = [0 for _ in range(n+1)]
    cap = 0
    answer = 0
    for pos in range(1, n+1):
        # 하차 처리
        cap -= t[pos]
        answer += t[pos]

        # 승차 처리
        try:
            # 현재 위치에서 출발하는 상자를 최대한 적재
            for box in sorted(boxes[pos]):
                # 자리가 모자란 경우 적재하려는 짐보다 나중에 도착하는 짐 중 가장 도착이 늦는 짐을 버림
                lack = max(cap+box[1]-c, 0)
                for p in range(n, box[0], -1):
                    if(lack == 0):
                        break
                    if(t[p]>0):
                        d = min(t[p], lack)
                        lack -= d
                        cap -= d
                        t[p] -= d
                l = box[1]-lack
                t[box[0]] += l
                cap += l
        except:
            None
    print(answer)


#1092 배
# 처음엔 박스 수를 크레인 수로 나누어 올림한 뒤
# 각 크레인이 옮기는 박스 수가 그 수를 벗어나면 다음 크레인으로 박스를 옮기는 식으로 구현
# 앞의 크레인과 분담 가능했던 박스도 뒤의 크레인이 부담해서 최솟값이 나오지 않는 문제 발생
# 크레인이 순서대로 자신이 들 수 있는 가장 무거운 박스를 옮기는 것을 박스가 모두 사라질 때까지 반복하는 그리디 알고리즘이 정답

# 번외: 걸리는 최소시간은 1분이며 최대시간은 박스 수 m분
# 또한 시간이 t분 걸린다고 가정할 때
# 각 크레인은 최대 t개의 박스만 옮겨야함
# 이를 이용하여 걸리는 시간에 대한 이진탐색으로 매우 빠른속도로 해결 가능
# 다음에는 이진탐색으로 다시 풀어볼것
def sol1092():
    n = int(input())
    crane = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    boxes = [0]*1000001
    min_val, max_val, sum_val = 1000001, 0, 0
    for i in map(int, input().split()):
        boxes[i] += 1
        min_val = min(min_val, i)
        max_val = max(max_val, i)
        sum_val += i
    
    if(crane[0]<max_val):
        print(-1)
        return
    else:
        time = 0
        while(sum_val>0):
            time += 1
            for c in crane:
                for i in range(c, min_val-1, -1):
                    if(boxes[i]>0):
                        boxes[i] -= 1
                        sum_val -= i
                        break 
        print(time)      


#15970 화살표 그리기
# 색깔별 점의 좌표들을 오름차순 정렬
# 각 점에서 가장 가까운 점과의 거리를 합산
# 점의 색이 두 개보다 많을 수 있음을 유의
def sol15970():
    n = int(input())
    arrows = {}
    for _ in range(n):
        p, c = map(int, input().split())
        try:
            arrows[c-1].append(p)
        except:
            arrows[c-1] = [p]
    
    answer = 0
    for arrow in arrows.values():
        arrow.sort()
        if(len(arrow)<2):
            continue
        answer += arrow[1]-arrow[0]
        answer += arrow[-1]-arrow[-2]
        for i in range(1, len(arrow)-1):
            answer += min(arrow[i]-arrow[i-1], arrow[i+1]-arrow[i])
    print(answer)


#9237 이장님 초대
# 각 나무가 다 자랄것으로 예상되는 날짜의 최댓값
def sol9237():
    n = int(input())
    trees = sorted(map(int, input().split()), reverse=True)
 
    print(max(trees[i]+i+1 for i in range(n))+1)