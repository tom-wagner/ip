def get_points(intervals):
    # this sorting doesn't work:
    # https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    intervals.sort(key=lambda x: (x[1], x[0]))

    points = []
    latest_endpoint = intervals[0][1]  # this throws an error when initialized as None

    for start, end in intervals:
        if start <= latest_endpoint:
            continue
        else:
            points.append(end)
            latest_endpoint = end

    return points


# print(get_points([(1, 3), (5, 7), (9, 12), (14, 17)]))  # [7, 12, 17]

// const test = [[1, 6], [2, 4], [9, 10], [-3, -2]];
// const test = [[1,6], [12,17], [-5, -3], [2, 3]];
const test = [[0, 100], [10, 90], [30, 50]];

def get_points_tom(intervals):
    earliest_end_time = sorted(intervals, key=lambda x: x[1])[0][1]
    latest_start_time = sorted(intervals, key=lambda x: x[0], reverse=True)[0][0]

    if earliest_end_time < latest_start_time:
        return [earliest_end_time, latest_start_time]
    return [earliest_end_time, earliest_end_time]


print(get_points_tom([(1, 3), (5, 7), (9, 12), (14, 17)]))  # [7, 12, 17]
print(get_points_tom([(1, 100), (8, 77), (12, 52), (17, 47)]))  # [7, 12, 17]
