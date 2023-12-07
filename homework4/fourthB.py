N = int(input())

col = [True] * N
row = [True] * N
diag1 = [True] * (2*N - 1)
diag2 = [True] * (2*N - 1)
count = 0


def foo(i):
    global count
    if i == N:
        count += 1
        return

    for j in range(N):
        if col[j] and row[i] and diag1[i+j] and diag2[j-i]:
            col[j] = False
            row[i] = False
            diag1[i+j] = False
            diag2[j-i] = False
            foo(i + 1)
            col[j] = True
            row[i] = True
            diag1[i + j] = True
            diag2[j - i] = True

foo(0)
print(count)
