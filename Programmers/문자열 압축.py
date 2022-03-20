# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for l in range(1, len(s) // 2 + 1):
        compression = ''
        count = 1
        for k in range(0, len(s), l):
            split1 = s[k:k + l]
            split2 = s[k + l:k + 2 * l]
            if split1 != split2:
                if count != 1:
                    compression += str(count) + split1
                    count = 1
                else:
                    compression += split1
            else:
                count += 1
        if answer > len(compression):
            answer = len(compression)
    return answer
