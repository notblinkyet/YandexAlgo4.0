def merge(nums1, nums2):
    res = []
    p1, p2 = 0, 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] <= nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
        else:
            res.append(nums2[p2])
            p2 += 1
    if p1 >= len(nums1):
        while p2 < len(nums2):
            res.append(nums2[p2])
            p2 += 1
    else:
        while p1 < len(nums1):
            res.append(nums1[p1])
            p1 += 1
    return res


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A)//2])
    R = merge_sort(A[len(A)//2:])
    return merge(L, R)

length = int(input())
nums = list(map(int, input().split()))
print(*merge_sort(nums))
