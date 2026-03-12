def parentheses(exp):
    x=[]
    brackets={')':'(','}':'{',']':'['}
    for i in exp:
        if i in "({[":
            x.append(i)
        elif i in ")}]":
            if not x or x[-1]!=brackets[i]:
                return "unbalanced"
            x.pop()
    if not bool(x):
        return "balanced"
    else:
        return "unbalanced"

x= parentheses("(()))(")
print(x)


# --------------------------------------------------


def to_postfix(exp):
    stack = []
    output = []
    pre = {'+':1, '-':1, '*':2, '/':2, "^":3}
    if parentheses(exp)=="balanced":
        for i in exp:
            if i.isalnum():
                output.append(i)

            elif i in "+-*/":
                while stack and stack[-1] != '(' and pre[stack[-1]] >= pre[i]:
                    output.append(stack.pop())
                stack.append(i)

            elif i == '(':
                stack.append(i)

            elif i == ')':
                while stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return " ".join(output)
    else:
        return False
    
y= to_postfix("(A+B)*C")
print(y)
y=y.split()
print(y)

# -----------------------------------------------------------------------

def eval_postfix(exp):
    stack = []

    for i in exp.split():
        if i.isdigit():
            stack.append(float(i))
        else:
            b = stack.pop()
            a = stack.pop()

            if i == '+': stack.append(a+b)
            if i == '-': stack.append(a-b)
            if i == '*': stack.append(a*b)
            if i == '/': stack.append(a/b)
            if i == '^': stack.append(a^b)

    return stack.pop()

evaluated=eval_postfix("3 4 + 2 * 7 /")
print(evaluated)

# ----------------------------------------------------------------------------

class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
root.left.right=Node(6)
root.right.left=Node(7)

def bfs(root):
    q=[]
    q.append(root)

    while q:
        x= q.pop(0)
        print(x.val, end=" ")

        if x.left:
            q.append(x.left)
        if x.right:
            q.append(x.right)


bfs(root)