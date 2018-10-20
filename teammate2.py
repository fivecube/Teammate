from collections import Counter

foo = {1: 1, 2: 1, 3: 3, 4: 3}
last = 3
MOD = 10**9 + 7
for x in range(5, 10**5, 2):
    p = (x*last) % MOD
    foo[x] = p
    foo[x+1] = p
    last = p

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = Counter(a)
    inds = {e: i for i, e in enumerate(a)}
    ans = 1
    for e, f in c.items():
        ans *= foo[f]
        if f % 2 == 0 and inds[e] % 2 == 0:
            ans *= f
        if ans > MOD:
            ans = ans % MOD
    print(ans % MOD)