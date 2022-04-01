# https://atcoder.jp/contests/abc031/submissions/30605648

A, D = map(int, input().split())

Offensive_power = (A + 1) * D
Defense_power = (D + 1) * A

if Defense_power == Offensive_power:
    print(Defense_power)

elif Offensive_power > Defense_power:
    print(Offensive_power)

elif Defense_power > Offensive_power:
    print(Defense_power)
