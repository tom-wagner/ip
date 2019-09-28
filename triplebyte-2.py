from typing import List
from collections import defaultdict

'''
We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period, and returns each time that they badged in during that period. (If there are multiple one-hour periods where this was true, just return the first one.)


badge_times = [
  ["Paul",     1355],
  ["Jennifer", 1910],
  ["John",      830],
  ["Paul",     1315],
  ["John",      835],
  ["Paul",     1405],
  ["Paul",     1630],
  ["John",      855],
  ["John",      930],
  ["John",      915],
  ["John",      730],
  ["Jennifer", 1335],
  ["Jennifer",  730],
  ["John",     1630],
]

# first one if there's multiple

Expected output (in any order)
  John:  830  835  855  915  930
  Paul: 1315 1355 1405

n: length of the badge records array

Return a dictionary of people who scanned into room 3 or more times within one hour period
- Return a list of all scans that encompassed the violation
'''


def get_violators(badge_records: List) -> List:
    room = set()
    did_not_scan_entry = set()
    did_not_scan_exit = set()

    for person, direction in badge_records:
        print(room)
        if (person in room) and (direction == 'enter'):
            did_not_scan_exit.add(person)
        if (person not in room) and (direction == 'exit'):
            did_not_scan_entry.add(person)

        if direction == 'exit' and person in room:
            room.remove(person)
        if direction == 'enter':
            room.add(person)

    # add people still in room to violators
    did_not_scan_exit = did_not_scan_exit.union(room)

    return [list(did_not_scan_entry), list(did_not_scan_exit)]


badge_times = [
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 835],
    ["Paul", 1405],
    ["Paul", 1630],
    ["John", 855],
    ["John", 930],
    ["John", 915],
    ["John", 730],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630],
]


def get_violations_for_person(times):
    back = 0
    for front, time in enumerate(times):
        print(back, front, time)
        # advance front pointer
        if times[back] + 100 >= times[front]:
            # advance back pointer
            while times[back] + 100 <= times[front]:
                back += 1
            continue
        if front - back >= 2:
            return times[back:front + 1]


print(get_violations_for_person([730, 830, 835, 855, 915, 930, 1630]))


def get_three_times(badge_records: List):
    sorted_badge_times = sorted(badge_records, key=lambda t: t[1])
    times = defaultdict(list)
    for person, time in sorted_badge_times:
        times[person].append(time)

    violators = {}
    for person, times in times.items():
        violations_for_person = get_violations_for_person(times)
        if violatons_for_person:
            violators[person] = violations_for_person

    return violators

# get_three_times(badge_times)

#       1         3
# [730, 830, 835, 855, 915, 930, 1630]