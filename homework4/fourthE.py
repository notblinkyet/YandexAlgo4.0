d = {"(": ")",
    "[": "]"
}

def generate_bracket_sequences(n):
    def backtrack(sequence, open_kv, close_kv, open_kr, close_kr, stack):
        if len(sequence) == n:
            result.append(sequence)
            return
        if open_kr + open_kv < n // 2:
            stack.append("(")
            backtrack(sequence + '(', open_kv, close_kv, open_kr + 1, close_kr, stack.copy())
            stack.pop()
        if open_kr + open_kv < n // 2:
            stack.append("[")
            backtrack(sequence + '[', open_kv + 1, close_kv, open_kr, close_kr, stack.copy())
            stack.pop()
        if close_kr < open_kr and stack[-1] == "(":
            stack.pop()
            backtrack(sequence + ')', open_kv, close_kv, open_kr, close_kr+1, stack.copy())
            stack.append("(")
        if close_kv < open_kv and stack[-1] == "[":
            stack.pop()
            backtrack(sequence + ']', open_kv, close_kv+1, open_kr, close_kr, stack.copy())
            stack.append("[")

    result = []
    backtrack('', 0, 0, 0, 0, [])
    return result

n = int(input())
if n % 2 == 0:
    sequences = generate_bracket_sequences(n)
    for sequence in sequences:
        print(sequence)
else:
    print()
