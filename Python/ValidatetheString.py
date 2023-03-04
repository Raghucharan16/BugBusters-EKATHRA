def is_valid(s):
    m = {')': '(', '}': '{', ']': '['}
    stack = []
    if len(s) % 2 == 0:
        for x in s:
            if x in '({[':
                stack.append(x)
            else:
                if not stack:
                    return False
                z = stack.pop()
                if x != m[z]:
                    return False
        return not stack
    else:
        return False

t = int(input())
for _ in range(t):
    s = input()
    if is_valid(s):
        print('YES')
    else:
        print('NO')
