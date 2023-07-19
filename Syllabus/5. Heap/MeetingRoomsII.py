import heapq


def meeting_rooms_II_heap(intervals):
    # declare variables
    start_times = []
    end_times = []
    meeting_rooms_counter = 0
    # populate start and end times
    for interval in intervals:
        start_times.append(interval[0])
        end_times.append(interval[1])

    # preprocess for computing meeting rooms
    start_times.sort()
    heapq.heapify(end_times)

    for start_time in start_times:
        if end_times[0] > start_time:
            meeting_rooms_counter += 1
        else:
            heapq.heappop(end_times)

    return meeting_rooms_counter


def meeting_rooms_II_count(intervals):
    """
    Works on O(n) time if intervals are limited in range. (usually the case)
    """

    # Helper functions for cleaner code

    def get_start(e):
        return e[0]

    def get_end(e):
        return e[1]

    # variables declaration

    minimum_start_time = min(intervals, key=lambda x: x[0])[0]
    maximum_end_time = max(intervals, key=lambda x: x[1])[1]

    start_times_counter = [0 for _ in range(maximum_end_time - minimum_start_time + 1)]
    end_times_counter = [0 for _ in range(maximum_end_time - minimum_start_time + 1)]

    meeting_room_count = 0

    # Count sort

    for interval in intervals:
        start_times_counter[get_start(interval) - minimum_start_time] += 1
        end_times_counter[get_end(interval) - minimum_start_time] += 1

    start_time_pointer = 0
    end_time_pointer = 0

    while start_time_pointer < len(start_times_counter):
        while (
            start_time_pointer < len(start_times_counter)
            and start_times_counter[start_time_pointer] == 0
        ):
            start_time_pointer += 1
        while (
            end_time_pointer < len(end_times_counter)
            and end_times_counter[end_time_pointer] == 0
        ):
            end_time_pointer += 1

        if start_time_pointer < len(start_times_counter) and end_time_pointer < len(
            end_times_counter
        ):
            if end_time_pointer > start_time_pointer:
                meeting_room_count += 1
            else:
                end_times_counter[end_time_pointer] -= 1
            start_times_counter[start_time_pointer] -= 1
    return meeting_room_count


print(meeting_rooms_II_count([[0, 30], [5, 10], [15, 20]]))
