import random

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    first_section_sum, second_section_sum, third_section_sum = A[0], A[2], sum(A[4:])
    i, j = 1, 3
    while i < len(A) - 4 and j < len(A) - 2:
        if first_section_sum == second_section_sum and first_section_sum == third_section_sum:
            print(first_section_sum, second_section_sum, third_section_sum)
            return True
        elif second_section_sum < third_section_sum:
            second_section_sum += A[j]
            j += 1
            third_section_sum -= A[j]
        elif first_section_sum < second_section_sum:
            first_section_sum += A[i]
            i += 1
            second_section_sum -= A[i]
        else:
            # second_section_sum > third_section_sum OR first_section_sum > second_section_sum
            # impossible to recover
            return False
    return False


# print(solution([1, 3, 4, 2, 2, 2, 1, 1, 2]))
for x in range(0, 1000):
    solution([random.randint(0, 5) for x in range(2, 12)])

