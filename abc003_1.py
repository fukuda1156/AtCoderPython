# https://atcoder.jp/contests/abc003/submissions/30398307

N = int(input())

salary = 0

for i in range(1, N + 1):
    salary += 10000 * i * 1 / N

print(int(salary))
