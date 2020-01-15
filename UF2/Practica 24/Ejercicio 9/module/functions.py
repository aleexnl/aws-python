def combinatorio(n, k):
        if k == 0:
            return 1
        if n == 0:
            return 0
        return combinatorio(n - 1, k - 1) + combinatorio(n - 1, k)
