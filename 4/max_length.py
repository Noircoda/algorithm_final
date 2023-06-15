def find_max_gold_length(n, formulas):

    A = [0] * (n + 1)
    B = [0] * (n + 1)

    for i in range(1, n + 1):
        a, k, b = formulas[i - 1]  # 第i個配方

        # A[i] max
        A[i] = max(A[i - 1], B[i - 1])

        # B[i] max
        B[i] = max(A[i - 1] + a - k * b, B[i - 1] + a)


    return max(A[n], B[n])

# 測試
formulas = [(5, 3, 2), (20, 33, 1), (30, 115, 1)]
n = len(formulas)

max_gold_length = find_max_gold_length(n, formulas)
print("最大黃金長度：", max_gold_length)
