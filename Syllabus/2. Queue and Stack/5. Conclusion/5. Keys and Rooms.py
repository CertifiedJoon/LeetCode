from collections import deque

def keysAndRooms(rooms):
  q = deque()
  q.append(0)
  visited = set()
  
  while q:
    rm_no = q.popleft()
    visited.add(rm_no)
    for key in rooms[rm_no]:
      if key not in visited:
        q.append(key)
  
  return len(visited) == len(rooms)

print(keysAndRooms([[1,3],[3,0,1],[2],[0]]))