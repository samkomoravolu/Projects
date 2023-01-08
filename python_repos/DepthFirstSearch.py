from queue import LifoQueue as Stack

def initr():
    m=[[1,2,3,4],[2,3],[0,1,4],[0,2,3],[1,3],[5,6],[5,6],[7]]
    return m

def dfs(m, s):
    visited = []
    curr = Stack()
    curr.put(s)
    while not curr.empty():
        node = curr.get()
        if node in visited:
            continue
        visited.append(node)
        for entry in m[node]:
            if entry not in visited:
                curr.put(entry)
    return visited

def dfsRec(m, s, visited):
    visited.append(s)
    for i in m[s]:
        if i not in visited:
            visited = dfsRec(m, i, visited)
    return visited

def count(m):
    visited = []
    count = 0
    while len(visited) < len(m):
        n = -1
        for i in range(len(m)):
            if i not in visited:
                n = i
                break
        new = dfs(m, n)
        for i in new:
            visited.append(i)
        count += 1
    return count
            

def main():
    m = initr()
    print(dfsRec(m, 0, []))
    print(dfs(m, 0))

main()
