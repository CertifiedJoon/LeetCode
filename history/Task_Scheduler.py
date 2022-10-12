class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        rep = {} #task:rep
        for t in tasks:
            if t not in rep:
                rep[t] = 1
            else:
                rep[t] += 1
        most = max(v for k,v in rep.items())
        num_most = len([k for k,v in rep.items() if v == most])
        return max(len(tasks), (most-1) * (n + 1) + num_most)
