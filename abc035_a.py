# https://atcoder.jp/contests/abc035/submissions/30606565

W, H = map(int, input().split())

if W % 16 == 0 and H % 9 == 0:
    print('16:9')

elif W % 4 == 0 and H % 3 == 0:
    print('4:3')
