def solution(numbers, k):
    # Type your solution here
    return sorted(numbers, reverse=True)[k - 1]


print(solution([1, 4, 3, 4, 2, 5], 3))
