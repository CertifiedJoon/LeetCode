class Solution:
    def GenerateParenthesis(self, n):
        result = []
        self.RecGenerateParenthesis([],n,n,result)
        print(result)
        return result

    def RecGenerateParenthesis(self, soFar, l, r, result):
        if not l and not r:
            result.append(''.join(soFar))
            return
        if len(l) == len(r):
            self.RecGenerateParenthesis(soFar + '(', l-1, r, result)
        else:
            if (len(l)):
                self.RecGenerateParenthesis(soFar + '(', l - 1, r, result)
            if (len(r)):
                self.RecGenerateParenthesis(soFar + ')', l, r-1, result)


Solution().GenerateParenthesis(3)