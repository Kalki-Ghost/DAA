"""The program to check the equation is balanced or not by parenthesis"""
import collections


def is_balanced(eq):
    stack = collections.deque()
    for i in eq:
        if i in ['(', '{', '[']:
            stack.append(i)
        elif i in [')', ']', '}']:
            if len(stack) == 0:
                return False
            sy = stack.pop()
            if sy == '(' and i == ')':
                continue
            elif sy == '{' and i == '}':
                continue
            elif sy == '[' and i == ']':
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    return False


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
