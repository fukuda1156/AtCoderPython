# https://atcoder.jp/contests/abc024/submissions/30546402

A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

Price = 0

Price += A * S + T * B

if S + T >= K:
    Price -= C * (S + T)

print(Price)
