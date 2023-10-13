def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def infix_to_prefix(expression):
    expression = expression[::-1]
    for i in range(len(expression)):
        if expression[i] == '(':
            expression = expression[:i] + ')' + expression[i+1:]
        elif expression[i] == ')':
            expression = expression[:i] + '(' + expression[i+1:]
    
    postfix = infix_to_postfix(expression)
    prefix = postfix[::-1]
    return prefix

# Example usage:
infix_expression = "a + b * (c - d) / e"
postfix_expression = infix_to_postfix(infix_expression)
prefix_expression = infix_to_prefix(infix_expression)

print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}")
print(f"Prefix: {prefix_expression}")
