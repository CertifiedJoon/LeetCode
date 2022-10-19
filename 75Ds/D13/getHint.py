class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        x = y = 0
        to_match_s = {}
        to_match_g = {}
        for s, g in zip(secret, guess):
            if s == g:
                x += 1
            else:
                if g in to_match_s and to_match_s[g]:
                    to_match_s[g] -= 1
                    y += 1
                else:
                    to_match_g[g] = to_match_g.get(g, 0) + 1
                
                if s in to_match_g and to_match_g[s]:
                    to_match_g[s] -= 1
                    y += 1
                else:
                    to_match_s[s] = to_match_s.get(s, 0) + 1

        return f"{str(x)}A{str(y)}B"