def string_compression(s):
    res = []
    last_idx_compressed = -1
    for idx, char in enumerate(s):
        if idx == len(s) - 1 or char != s[idx + 1]:
            consecutive_chars_count = idx - last_idx_compressed
            res.append(f'{char}{consecutive_chars_count}')
            last_idx_compressed = idx
    compressed = ''.join(res)
    return compressed if len(compressed) < len(s) else s
