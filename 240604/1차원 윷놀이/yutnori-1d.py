n, m, k = list(map(int, input().split()))
moves = list(map(int, input().split()))

# moves를 n개의 말에 배분하는 조합

answers = [[0] for _ in range(k)]

def choose(count):
    if count == 4:
        print(answers)
        return

    for i in len(moves):
        answers[j].append(moves[i])
        t = moves.pop()
        choose(count + 1)
        answers[j].pop()
        moves.append(t)

    return

choose(0)