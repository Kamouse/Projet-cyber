def evalRPN(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(int(num1 / num2))
    return stack[0]

expression = "122 82 88 + 5 - *"
result = evalRPN(expression)
print(result)