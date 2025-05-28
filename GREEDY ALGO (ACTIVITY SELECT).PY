def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    last_end = activities[0][1]
    count = 1
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
    return count

print(activity_selection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))  # 4
#Time Complexity: O(n log n)


