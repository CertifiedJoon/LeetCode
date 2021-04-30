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
        if l == r:
            self.RecGenerateParenthesis(soFar + ['('], l-1, r, result)
        else:
            if (l):
                self.RecGenerateParenthesis(soFar + ['('], l - 1, r, result)
            if (r):
                self.RecGenerateParenthesis(soFar + [')'], l, r-1, result)
    def NoRecGenerateParenthesis(self, n):
        result = []
        soFar = []
        l = r = n
        while(True):
            if not l and not r:
                result.append(''.join(soFar))
                l + 1 

while(True):
    i = int(input())
    Solution().GenerateParenthesis(i)