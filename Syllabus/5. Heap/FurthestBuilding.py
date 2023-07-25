import heapq


def furthest_building(heights, bricks, ladders):
    buildings_reached = []
    previous_height = heights[0]
    for i, height in enumerate(heights):
        if height > previous_height:
            height_difference = height - previous_height
            heapq.heappush(buildings_reached, -height_difference)
            if bricks > height_difference:
                bricks -= height - previous_height
                # max heap implemented with min heap
            else:
                if ladders > 0:
                    # since we store the negative of height difference
                    bricks -= heapq.heappop(buildings_reached)
                    ladders -= 1
                else:
                    return i - 1

    return len(heights) - 1


print(furthest_building([14, 3, 19, 3], 17, 0))
