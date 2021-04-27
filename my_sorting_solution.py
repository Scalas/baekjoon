import sys

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
