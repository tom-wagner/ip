from collections import Counter


def palindrome_permutation(string):
    counts = Counter(string)
    del counts[' ']
    odd_counts = {char: count for char, count in counts.items() if count % 2 != 0}
    return len(odd_counts) <= 1


print(palindrome_permutation('taco cat'))
