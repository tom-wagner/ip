def stairs_recursive_dynamic(n):
    memo = {}

    def recurse(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif memo.get(n):
            return memo[n]

        res = recurse(n - 1) + recurse(n - 2)
        memo[n] = res
        return res

    return recurse(n)


def stairs_bottom_up_dynamic(n):
    memo, curr = {1: 1, 2: 2}, 3

    while curr <= n:
        memo[curr] = memo[curr - 1] + memo[curr - 2]
        curr += 1

    return memo[n]


print(stairs_recursive_dynamic(500))
print(stairs_bottom_up_dynamic(500))
