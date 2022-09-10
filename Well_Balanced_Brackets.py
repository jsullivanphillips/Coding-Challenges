
left_braces = ['(', '[', '{']
right_braces = [')',']','}']
stack = []

def my_function(input):
    for char in input:
        if char in left_braces:
            stack.append(char)
        if char in right_braces:
            if char == ')':
                if stack.pop() == '(':
                    return True
                else:
                    return False
            if char == ']':
                if stack.pop() == '[':
                    return True
                else:
                    return False
            if char == '}':
                if stack.pop() == '{':
                    return True
                else:
                    return False

test_1 = '({[]})'
print(my_function(test_1))
