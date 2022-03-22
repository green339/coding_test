# https://programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    answer = []
    sharps = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}
    for music in musicinfos:
        s, e, n, i = music.split(",")
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        t = (eh - sh) * 60 + em - sm
        for k, v in sharps.items():
            i = i.replace(k, v)
            m = m.replace(k, v)
        play = i * (t // len(i))
        play += i[:t % len(i)]
        if m in play:
            if answer and answer[1] >= t:
                continue
            answer = [n, t]
    return answer[0] if answer else "(None)"
