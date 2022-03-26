# https://atcoder.jp/contests/abc014/submissions/30487961

a = int(input())
b = int(input())

c = a % b

if c == 0:
    print(0)
if c != 0:
    print(b - c)
