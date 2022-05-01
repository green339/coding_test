# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              "*": (3, 0), 0: (3, 1), "#": (3, 2)}
    cl = (3, 0)
    cr = (3, 2)
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
        else:
            ml = abs(cl[0] - keypad[n][0]) + abs(cl[1] - keypad[n][1])
            mr = abs(cr[0] - keypad[n][0]) + abs(cr[1] - keypad[n][1])
            if ml > mr:
                answer += 'R'
            elif ml < mr:
                answer += 'L'
            else:
                if hand == "right":
                    answer += 'R'
                else:
                    answer += 'L'
        if answer[-1] == 'R':
            cr = keypad[n]
        else:
            cl = keypad[n]
    return answer
