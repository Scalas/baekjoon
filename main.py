import sys

input = sys.stdin.readline
out = sys.stdout.write


def sol5635():
    n = int(input())
    stdt = [input().split() for _ in range(n)]
    youngest = max(stdt, key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
    oldest = min(stdt, key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
    out('\n'.join((youngest[0], oldest[0])))
    
    
sol5635()