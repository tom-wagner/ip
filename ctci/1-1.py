def is_unique(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True


def is_unique_in_place(string):
    s = sorted(string)
    for idx, char in enumerate(s):
        if idx == 0:
            continue
        if s[idx - 1] == s[idx]:
            return False
    return True


# def is_unique_in_place(s):
#     return sum([1 if s[idx - 1] == s[idx] else 0 for idx, char in enumerate(sorted(s)[1:])]) == len(s)

print(is_unique_in_place('dfsijsk'))
