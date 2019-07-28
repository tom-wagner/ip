from helpers.thieves_solution import thieves_solution

# THIEVES KNAPSACK

#        NAME, WEIGHT, VALUE (for this weight)
items = [("beef",    3.8, 36.0),
         ("pork",    5.4, 43.0),
         ("ham",     3.6, 90.0),
         ("greaves", 2.4, 45.0),
         ("flitch",  4.0, 30.0),
         ("brawn",   2.5, 56.0),
         ("welt",    3.7, 67.0),
         ("salami",  3.0, 95.0),
         ("sausage", 5.9, 98.0)]

MAXWT = 15.0


def thieves(items, max_wt):
    pass


ans = thieves_solution(items, MAXWT)

print(ans == thieves(items, MAXWT))




