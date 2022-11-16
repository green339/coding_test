# https://school.programmers.co.kr/learn/courses/30/lessons/135807
def solution(arrayA, arrayB):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def get_gcd(arr):
        g = arr[0]
        for i in range(1, len(arr)):
            g = gcd(g, arr[i])
        return g

    def not_divide(arr, num):
        for a in arr:
            if not a % num:
                return 0
        else:
            return num

    A = get_gcd(arrayA)
    B = get_gcd(arrayB)
    return max(not_divide(arrayA, B), not_divide(arrayB, A))
