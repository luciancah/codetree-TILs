n = int(input())
answer = []
a2 = []

def is_beautiful():
    i = 0
    while i < n:
        if i + seq[i] - 1 >= n:
            return False
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
            
        i += seq[i]
        
    return True


def choose(curr_num):
    if curr_num == n + 1:
        if is_beautiful(answer):
            if is_beautiful(answer):
                a2.append(answer[:])
        return

    for i in range(1, 5):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)

print(len(a2))