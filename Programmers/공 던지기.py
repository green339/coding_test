# https://school.programmers.co.kr/learn/courses/30/lessons/120843
def solution(numbers, k):
    if len(numbers) % 2:
        tmp = (k - 1) % len(numbers)
        if tmp > len(numbers) // 2:
            tmp -= len(numbers) // 2
            return numbers[2 * tmp - 1]
        else:
            return numbers[2 * tmp]
    else:
        return numbers[2 * ((k - 1) % (len(numbers) // 2))]


def solution_v2(numbers, k):
    return numbers[(2 * (k - 1)) % len(numbers)]
