# https://atcoder.jp/contests/abc028/submissions/30572775

N = int(input())

if N == 100:
    print('Perfect')

elif 90 <= N <= 99:
    print('Great')

elif 60 <= N <= 89:
    print('Good')

else:
    print('Bad')
