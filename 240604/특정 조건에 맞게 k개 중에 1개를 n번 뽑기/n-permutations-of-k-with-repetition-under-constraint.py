k, n = tuple(map(int, input().split()))
answer = []

def print_answer():
    for e in answer:
        print(e, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(1, k+1):
        if curr_num >= 2 and answer[i-2] == answer[i-1] == i:
            continue
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)