length1 = int(input())
nums = list(map(int, input().split()))
pivot = int(input())
def treepointpart(l, r, x):
    n, g, e = l, l, l
    while n <= r:
        if nums[n] < x:
            nums[g], nums[e], nums[n] = nums[e], nums[n], nums[g]
            e += 1
            g += 1
        elif nums[n] == x:
            nums[g], nums[n] = nums[n], nums[g]
            g += 1
        n += 1
    return e, g

e, g = treepointpart(0, length1-1, pivot)
res2 = length1 - e
print(e, res2, sep="\n")