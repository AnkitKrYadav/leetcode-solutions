class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(eval(str(b)+i+str(a))))
            else:
                stack.append(int(i))
        return stack[0]