def is_rotation(x, y):
    if x == '' or y == '':
        return False
    if len(x) != len(y):
        return False

    first_char = x[0]
    for idx, char in enumerate(y):
        if char == first_char:
            prefix_from_y, suffix_from_y = y[:idx], y[idx:]
            prefix_from_x , suffix_from_x= x[0:len(suffix_from_y)], x[len(suffix_from_y):]

            if suffix_from_y == prefix_from_x and prefix_from_y == suffix_from_x:
                return True

    return False


print(is_rotation('waterbottle', 'erbottlewat'))
