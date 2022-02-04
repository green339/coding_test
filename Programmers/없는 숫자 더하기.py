# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = sum(set(nums) - set(numbers))
    return answer
