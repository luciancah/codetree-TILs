n = int(input())
answer = []
a2 = []

def is_beautiful(num_arr):
    flag = True
    i = 0
    while i < len(num_arr):
        temp = num_arr[i]
        count = 0
        for j in range(i, i + temp):
            if j >= len(num_arr):
                flag = False
                break
            if num_arr[j] == temp:
                count += 1
        if count != temp:
            flag = False
        i += temp
    return flag


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