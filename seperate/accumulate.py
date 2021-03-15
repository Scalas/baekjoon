# 2167 2차원 배열의 합
# 2차원배열의 누적합을 활용
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    sum_ij = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        line = list(map(int, input().split()))
        for j in range(1, m+1):
            sum_ij[i][j] = sum_ij[i-1][j]+sum_ij[i][j-1]-sum_ij[i-1][j-1]+line[j-1]
    k = int(input())
    case = [list(map(int, input().split())) for _ in range(k)]
    answers = []
    for i, j, x, y in case:
        answer = sum_ij[x][y] - sum_ij[i-1][y] - sum_ij[x][j-1] + sum_ij[i-1][j-1]
        answers.append(str(answer))
    print('\n'.join(answers))
solution()