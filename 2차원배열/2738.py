# https://www.acmicpc.net/problem/2738

ll = []
rl = []

n,m = map(int, input().split())

for _ in range(n): 
    t = list(map(int, input().split()))
    ll.append(t)

for _ in range(n) : 
    t = list(map(int, input().split()))
    rl.append(t)

for y in range(n):
    for x in range(m):
        print(ll[y][x]+rl[y][x], end=" ")
    print()
    
    
