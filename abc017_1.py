# https://atcoder.jp/contests/abc017/submissions/30511577

l = [list(map(int, input().split())) for l in range(3)]

total = 0

for i, i2 in l:
    total += i * i2 * 0.1

print(int(total))
