class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            if each in ["+", "-", "/", "*"]:
                val2, val1 = stack[-1], stack[-2]
                stack.pop()
                stack.pop()
                match each:
                    case "+":
                        stack.append(val1 + val2)
                    case "-":
                        stack.append(val1 - val2)
                    case "*":
                        stack.append(val1 * val2)
                    case "/":
                        stack.append(int(val1 / val2))
            else:
                stack.append(int(each))
        return stack[-1]
                


                
        