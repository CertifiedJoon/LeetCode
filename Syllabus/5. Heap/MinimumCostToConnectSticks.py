import heapq


def minimum_cost_to_connect_sticks(sticks):
    heapq.heapify(sticks)
    cost = 0

    while len(sticks) > 1:
        x, y = heapq.heappop(sticks), heapq.heappop(sticks)
        cost += x + y
        heapq.heappush(sticks, x + y)

    return cost
