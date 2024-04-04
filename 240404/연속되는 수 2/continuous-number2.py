n = int(input())
numbers = []
for i in range(n):
    numbers += input()

counts = []
count = 0

for i in range(len(numbers)):
    if i == 0:
        counts.append(1)
    if numbers[i] == numbers[i-1]:
        count += 1
        if i == len(numbers) - 1:
            counts.append(count)
    else:
        counts.append(count)
        count=1

print(max(counts))