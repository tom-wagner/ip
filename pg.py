def get_preceding_length(idx, nonrepeating_substr_at_each_idx):
    return 1 if idx - 1 < 0 else nonrepeating_substr_at_each_idx[idx - 1] + 1


def solution(s):
    last_seen_at = {}
    nonrepeating_substr_at_each_idx = [None for _ in range(len(s))]
    for idx, char in enumerate(s):
        if char not in last_seen_at:
            nonrepeating_substr_at_each_idx[idx] = get_preceding_length(idx, nonrepeating_substr_at_each_idx)
        else:
            char_last_seen_at = last_seen_at.get(char)
            nonrepeating_substr_at_each_idx[idx] = idx - char_last_seen_at
        last_seen_at[char] = idx
    return nonrepeating_substr_at_each_idx

