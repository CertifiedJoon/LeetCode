from typing import *
import heapq


def min_fueling(target: int, startFuel: int, stations: List[int]):
    pq = []  # heap for storing past 'unfueled' stations
    stations.append([target, 0])
    prevStation = 0
    remainingFuel = startFuel
    minStations = 0

    for position, gas in stations:
        remainingFuel -= position - prevStation

        while remainingFuel < 0 and pq:
            remainingFuel += -heapq.heappop(pq)
            minStations += 1

        if remainingFuel < 0:
            return -1

        heapq.heappush(pq, -gas)
        prevStation = position

    return minStations


print(min_fueling(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
