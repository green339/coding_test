from itertools import permutations


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


def solution(numbers):
    answer = set()
    numbers = list(str(numbers))
    for r in range(1, len(numbers) + 1):
        for p in set(permutations(numbers, r)):
            candidate = int(''.join(p))
            if is_prime(candidate):
                answer.add(candidate)
    return len(answer)
