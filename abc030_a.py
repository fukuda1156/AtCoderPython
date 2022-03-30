# https://atcoder.jp/contests/abc030/submissions/30573513

A, B, C, D = map(int, input().split())

Team_TAKAHASHI = B / A
Team_AOKI = D / C

if Team_TAKAHASHI == Team_AOKI:
    print('DRAW')

elif Team_TAKAHASHI >= Team_AOKI:
    print('TAKAHASHI')

elif Team_TAKAHASHI <= Team_AOKI:
    print('AOKI')
