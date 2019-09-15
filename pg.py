import collections
# welcome
# ~
#
# You
# are
# going
# to
# a
# flower
# shop and buying
# a
# bouquet
# of
# flowers
# several
# kinds
# of
# flowers
# e.g.red
# blue
# yellow
# how
# many
# types
# of
# bouquet
# you
# can
# build
# from the given
#
# colors
# of
# flowers
#
# 1.
# there is no
# concept
# of
# size
# 1
# red
# flower = 2
# red
# flowers
# same
# type
#
# input - red
# blue
# yellow
# output - ? r
# b
# y
# rb
# ry
# by
# rby
#
# 1 --> 1
# r
# 2 --> 3
# r
# b
# rb
# 2! + 1
# 3 --> 7
# r
# b
# y
# rb
# ry
# by
# rby
# 3! + 1
# 4 --> X
# r
# b
# y
# g
#
# 4 * 3 * 2 * 1 = 24
#
# n! -> r
# b
# y
# g
# -> b
# r
# y
# g(duplicate)
#
# r
# b(no
# b & r)
# slot1
# slot2
#
# entry
# 1
# red
# 2
# blue
# 3
# yellow
# exit
#
# n = 3
# r
# b
# y
# rb
# ry
# by
# rby
#
# 2.
# by
# given
# number
# of
# color(n), give
# me
# all
# types
# of
# bouquet
#
#
# # no flowers        OR r
# # no flowers y OR ry r


def get_updated_bouqets(current_bouquets, current_flower):
    if len(current_bouquets) == 0:
        return [current_flower]
    return [b + [current_flower] for b in current_bouquets]


def pick_flowers(n):
    # [0, 1, 2]
    flowers = list(range(n))
    bouquets = []

    def recurse(flower_options, current_bouquets, idx):
        if idx == len(flower_options):
            bouquets.extend(current_bouquets)
            return

        # look at the next flower option
        current_flower = flower_options[idx]

        # recurse with keeping flower
        updated_bouquets = get_updated_bouqets(current_bouquets, current_flower)
        recurse(flower_options, updated_bouquets, idx + 1)

        # recurse without keeping flower
        recurse(flower_options, current_bouquets, idx + 1)

    recurse(flowers, [], 0)
    return bouquets


def pick_flowers(n):
    flowers = list(range(n))
    idx = 1
    combinations = [[], [0]]

    while idx < len(flowers):
        curr_flower = flowers[idx]
        new_combos = [[combination, combinations + [curr_flower]] for combination in combinations]
        combinations = [item for sublist in new_combos for item in sublist]
        print(combinations)
        idx += 1

    return combinations


print(pick_flowers(3))

# so you go to a flower shop

# and there are N different color roses available
