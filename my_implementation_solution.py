import sys
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