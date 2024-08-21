class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetingRoomCnt = 0
        maxMeetingRoomCnt = 0
        intervals.sort()
        endQueue = []

        for start, end in intervals:
            while endQueue and endQueue[0] <= start:
                heapq.heappop(endQueue)
                meetingRoomCnt -= 1

            heapq.heappush(endQueue, end)
            meetingRoomCnt += 1
            maxMeetingRoomCnt = max(meetingRoomCnt, maxMeetingRoomCnt)

        return maxMeetingRoomCnt


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        usedRooms = 0

        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        l = len(intervals)

        endPointer = 0
        startPointer = 0

        while startPointer < l:
            if starts[startPointer] >= ends[endPointer]:
                usedRooms -= 1
                endPointer += 1

            usedRooms += 1
            startPointer += 1

        return usedRooms
