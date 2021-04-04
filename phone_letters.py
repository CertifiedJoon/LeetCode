class Solution:
    ret = list()
    dtol = { '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', 
             '7' : 'prqs', '8' : 'tuv', '9' : 'wxyz' }
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.ret = []
        if not digits:
            return list()
        self.lettersPermute('', digits)
        return self.ret
        
    def lettersPermute(self, SoFar, remaining):
        if (remaining == ''):
            self.ret.append(SoFar)
        else:
            for j in range(len(self.dtol[remaining[0]])):
                self.lettersPermute(SoFar + self.dtol[remaining[0]][j], remaining[1:])
