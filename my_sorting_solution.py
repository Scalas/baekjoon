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