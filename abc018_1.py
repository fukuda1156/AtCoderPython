# https://atcoder.jp/contests/abc018/submissions/19516899

ABC = [int(input()) for i in range(3)]

s = sorted(ABC)[::-1]

for i in ABC:
    print(s.index(i) + 1)
