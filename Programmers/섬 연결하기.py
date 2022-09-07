# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[-1])
    visited = set()
    visited.add(costs[0][0])
    while len(visited) != n:
        for i, j, c in costs:
            if i in visited and j not in visited:
                visited.add(j)
                answer += c
                break
            if i not in visited and j in visited:
                visited.add(i)
                answer += c
                break
    return answer
