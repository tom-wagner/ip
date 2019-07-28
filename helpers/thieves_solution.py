#        NAME, WEIGHT, VALUE (for this weight)


def thieves_solution(items, max_wt):
    sorted_items = sorted(((value / amount, amount, name)
                           for name, amount, value in items),
                          reverse=True)

    wt = val = 0
    bagged = []
    for unit_value, amount, name in sorted_items:
        portion = min(max_wt - wt, amount)
        wt += portion
        addval = portion * unit_value
        val += addval
        bagged += [(name, portion, addval)]
        if wt >= max_wt:
            break
    return bagged



