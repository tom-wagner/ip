# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def get_walking_direction(AX, AY, BX, BY):
    if AX == BX:
        return 'SOUTH' if AY > BY else 'NORTH'
    if AY == BY:
        return 'EAST' if AX > BX else 'WEST'
    if AX < BX:
        return 'SOUTHEAST' if AY > BY else 'NORTHEAST'
    elif AX > BX:
        return 'SOUTHWEST' if AY > BY else 'NORTHWEST'


def lowest_common_multiple(x, y):
    print(x, y)
    greater = max(x, y)
    print(greater)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1
    return greater


def greatest_common_factor(x, y):
    abs_x, abs_y = abs(x), abs(y)
    smaller, larger = min(abs_x, abs_y), min(abs_x, abs_y)
    curr = smaller
    while curr > 0:
        if smaller % curr == 0 and larger % curr == 0:
            return curr
        curr -= 1
    return None


def solution(AX, AY, BX, BY):
    # write your code in Python 3.6
    walking_direction = get_walking_direction(AX, AY, BX, BY)
    if walking_direction == 'NORTH':
        return f'{BX + 1},{BY}'
    elif walking_direction == 'SOUTH':
        return f'{BX - 1},{BY}'
    elif walking_direction == 'EAST':
        return f'{BX},{BY - 1}'
    elif walking_direction == 'WEST':
        return f'{BX},{BY + 1}'

    slope = (AY - BY) / (AX - BX) if (walking_direction != 'NORTH' and walking_direction != 'SOUTH') else 0
    delta_x, delta_y = AX - BX, AY - BY
    shortest_distance = greatest_common_factor(delta_x, delta_y) or lowest_common_multiple(delta_x, delta_y)

    if walking_direction == 'NORTHEAST':
        if slope >= 1:
            rise, run = slope / shortest_distance, shortest_distance
        else:
            rise, run = shortest_distance, slope / shortest_distance
        return f'{BX + run},{BY - rise}'
    elif walking_direction == 'SOUTHEAST':
        if slope >= -1:
            rise, run = slope / shortest_distance, shortest_distance
        else:
            rise, run = shortest_distance, slope / shortest_distance
        return f'{BX - run},{BY - rise}'
    elif walking_direction == 'SOUTHWEST':
        pass
        # return f'{},{}'
    elif walking_direction == 'NORTHWEST':
        pass
        # return f'{},{}'


# print(solution(-1, 3, 3, 1))

print(solution(2, 2, 2, -3))

# print(lowest_common_multiple(3, 8))
