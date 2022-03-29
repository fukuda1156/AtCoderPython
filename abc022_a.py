# https://atcoder.jp/contests/abc022/submissions/30546048

N, S, T = map(int, input().split())

weight_list = []

for _ in range(N):
    weight_list.append(int(input()))

weight = 0
answer = 0

for i in weight_list:
    weight += i
    if S <= weight <= T:
        answer += 1
print(answer)
