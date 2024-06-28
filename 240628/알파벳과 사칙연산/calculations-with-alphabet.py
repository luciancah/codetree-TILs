nums = [0 for _ in range(6)]
exp = input()

def conv(char):
    # a -> 0, f -> 5
    return ord(char) - ord('a')

def calc():
    value = nums[conv(exp[0])]
    for i in range(2, len(exp), 2):
        if exp[i-1] == '+':
            value += nums[conv(exp[i])]
        elif exp[i-1] == '-':
            value -= nums[conv(exp[i])]
        else:
            value *= nums[conv(exp[i])]
    return value

ans = 0
def recur(count):
    global ans
    if count == len(exp):
        ans = max(ans, calc())
        return
    
    for i in range(1, 5):
        nums[count] = i
        recur(count+1)

recur(0)
print(ans)