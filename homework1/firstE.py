def radix_sort(A, n):
    for i in range(n):
        buckets = [[] for _ in range(10)]
        for num in A:
            buckets[int(num) // 10**i % 10].append(num)
        A = []
        print(f"Phase {i+1}")
        for j in range(10):
            if buckets[j]:
                print(f"Bucket {j}:", end=" ")
                print(*buckets[j], sep=", ")
                A.extend(buckets[j])
            else:
                print(f"Bucket {j}: empty")
        print("**********")
    return A


count = int(input())
nums = []
num1 = input()
nums.append(num1)
for _ in range(count-1):
    nums.append(input())
print("Initial array:")
print(*nums, sep=", ")
print("**********")
res = radix_sort(nums, len(num1))
print("Sorted array:")
print(*res, sep=", ")
