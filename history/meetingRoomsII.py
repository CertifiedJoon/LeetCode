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
