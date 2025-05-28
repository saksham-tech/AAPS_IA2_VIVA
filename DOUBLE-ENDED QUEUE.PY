from collections import deque
dq = deque()
dq.appendleft(1)
dq.append(2)
dq.appendleft(3)
dq.append(4)
print(list(dq))  # [3, 1, 2, 4]

#Time Complexity: O(1)
