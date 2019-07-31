def coin_sum(amt, coins):
    c = coins[::-1]
    memo = {}

    def recurse(tgt, options):
        key_for_memo = f'{tgt} + {options}'
        if tgt == 0:
            return 1
        if key_for_memo in memo:
            return memo[key_for_memo]

        res = sum([
            recurse(tgt - coin, options[idx:])
            for idx, coin in enumerate(options)
            if tgt - coin >= 0
        ])
        memo[key_for_memo] = res
        return res

    return recurse(amt, c)


print(coin_sum(10, [1, 5, 10, 25]))
