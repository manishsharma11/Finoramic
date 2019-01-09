class Solution:
    def braces(self, A):
        Stack = []
        for s in A: 
            if s == ')':  
                top = Stack.pop()
                x = 0
                while top != '(':  
                    x += 1
                    top = Stack.pop()  
                if x <= 1:  
                    return 1
            else: 
                Stack.append(s)  
        return 0