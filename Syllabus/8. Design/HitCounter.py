"""
Premise:
1. Hit counter stores hits and retrieves hit count within 5 minute window
2. HitCounter.hit(int timestamp) timestamp in seconds
3. HitCounter.getHits(int timetstamp)

Assumptions:
1. all timestamps are monotonically increasing
2. Several ( or many ) hits in a second.

Constraints:
1. 1 <= timestamp <= 2*10^9
2. A ton of calls within a minute (introduce buffer + hitcounter for the current timestamp)

States (instance & class variables):
1. timestamp_and_hits (deque((timestamp, hits))) stores hits per the specific timestamp 
2. buffer_hit_count (int) stores the hits for the current timestamp.
3. buffer_timestamp (int) stores the current timestamp.
3. hit_counter (int) 

Logic
1. HitCounter.hit() -> if timestamp == buffer_timestamp, increment buffer_count, else append (buffer_timestamp, buffer_count) to timestamp_and_hits.
2. HitCounter.getHits() -> popleft until timestamp - 300, update the hit_counter per each pop, and return the hit_counter + buffer_counter.
3. HitCounter.HitCounter -> init timestamp_and_hits, buffer_count = 0, buffer_timestamp = 0, hit_counter.
"""

from collections import deque


class HitCounter:
    def __init__(self):
        # stores (timestamp, hit_count) in a deque
        self._timestamp_and_hits = deque()
        # stores the hit_count for the current time (last timestamp recorded)
        self._buffer_hit_count = 0
        # stores the timestamp for the current time (last timestamp recorded)
        self._buffer_timestamp = 0
        # total hit_count for the five minute window
        self._hit_count = 0

    def hit(self, timestamp: int) -> None:
        # if the timestamp did not change from the buffer timestamp, increment buffer hit count
        # else 'flush' the buffer to the deque.
        if timestamp == self._buffer_timestamp:
            self._buffer_hit_count += 1
        else:
            self._timestamp_and_hits.append(
                (self._buffer_timestamp, self._buffer_hit_count)
            )
            self._hit_count += self._buffer_hit_count
            self._buffer_timestamp = timestamp
            self._buffer_hit_count = 1

    def getHits(self, timestamp: int) -> int:
        if self._timestamp_and_hits:
            old_timestamp, old_hit_count = self._timestamp_and_hits[0]
        else:
            return (
                self._buffer_hit_count
                if self._buffer_timestamp <= timestamp - 300
                else 0
            )
        while old_timestamp <= timestamp - 300:
            self._hit_count -= old_hit_count
            self._timestamp_and_hits.popleft()
            if self._timestamp_and_hits:
                old_timestamp, old_hit_count = self._timestamp_and_hits[0]
            else:
                break
        return self._buffer_hit_count + self._hit_count
