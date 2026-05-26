n = int(input())
lst = list(map(int, input().split()))
ans = [0]
summ = sum(lst)
mini = [summ]
mid = mini[0] // 2


def dfs(i, summ):
    if i == n:
        if abs(mid-summ) < mini[0]:
            ans[0] = summ
            mini[0] = abs(mid-summ)
        return
    dfs(i+1, summ)
    dfs(i+1, summ + lst[i])


dfs(0, 0)
print(abs(summ - 2*ans[0]))
