from collections import Counter, defaultdict

st = input()
cnt = Counter(st)
n = len(st)
st = sorted(list(set(st)))
ans = []

def dfs(s, c):
    if len(s) == n:
        ans.append(''.join(s))
        return
    for val in st:
        if cnt[val] != c[val]:
            c[val] += 1
            dfs(s+val, c)
            c[val] -= 1


dfs('', defaultdict(int))
print(len(ans))
for i in ans: print(i)