import random

length = int(input())

if length == 0:
    print()
else:
    nums = list(map(int, input().split()))

    def choose(l, r):
        m = (r - l)//2
        a, b, c = nums[l], nums[r], nums[m]
        return (a + b + c) - min(a, b, c) - max(a, b, c)


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


    def quicksort(l, r):
        if l < r:
            pivot = random.randint(l, r)
            e, g = treepointpart(l, r, pivot)
            quicksort(l, e - 1)
            quicksort(g, r)
    quicksort(0, length - 1)
    print(*nums)
