import sys

N = int(sys.stdin.readline().strip())
expr = sys.stdin.readline().strip()
stack = []
nums = []
operand1 = 0
operand2 = 0

for i in range(N):
    nums.append(float(sys.stdin.readline().strip()))

for i in expr:
    if i.isalpha():
        stack.append(nums[ord(i)-65])
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if i == '+':
            stack.append(operand1+operand2)
        elif i == '-':
            stack.append(operand1-operand2)
        elif i == '*':
            stack.append(operand1*operand2)
        elif i == '/':
            stack.append(operand1/operand2)
print("{:.2f}".format(stack.pop()))