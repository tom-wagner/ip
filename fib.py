def nth_f(n):
    memo = {}

    def r(n):
        if n == 1 or n == 2:
            return 1
        elif memo.get(n):
            return memo.get(n)

        res = r(n - 1) + r(n - 2)
        memo[n] = res
        return res

    return r(n)

for x in range(1, 10):
    print(nth_f(x))