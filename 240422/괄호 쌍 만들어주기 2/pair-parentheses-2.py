input_string = input()
count = 0

for i in range(len(input_string)):
    if input_string[i] == '(' and input_string[i+1] == '(':
        for j in range(i+2, len(input_string)):
            if input_string[j-1] == ')' and input_string[j] == ')':
                count += 1

print(count)