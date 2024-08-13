class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Premise
        . given intervals, find minimum number of intervals to remove

        Constraint
        . 1 <= intervals.len <= 100,000
        . -50000 <= start < end <= 50000
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        occupiedRange = (intervals[0][0], intervals[0][1])

        for interval in intervals[1:]:
            start, end = interval
            if start < occupiedRange[1]:
                count += 1
            else:
                occupiedRange = (occupiedRange[0], end)
        return count
