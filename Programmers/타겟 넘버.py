# https://programmers.co.kr/learn/courses/30/lessons/43165
def dfs(depth, total):
    if depth == len(nums):
        if total == goal:
            return 1
        else:
            return 0
    else:
        return dfs(depth + 1, total - nums[depth]) + dfs(depth + 1, total + nums[depth])


def solution(numbers, target):
    global nums, goal
    nums = numbers
    goal = target
    return dfs(0, 0)
