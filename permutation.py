class Solution:
    def permute(self, nums):
        ret = []
        self._recPermute([], nums, ret)
        return ret
    def _recPermute(self, soFar, remaining, ret):
        if not remaining:
            ret.append(soFar)
        
        for i in range(len(remaining)):
            self._recPermute(soFar + [remaining[i]], remaining[:i] + remaining[i + 1:], ret)