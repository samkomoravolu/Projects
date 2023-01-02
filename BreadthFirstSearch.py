from queue import Queue

def initr():
    m=[[1,2,3,4],[2,3],[0,1,4],[0,2,3],[1,3],[5,6],[5,6],[7]]
    return m

def bfs(m, s):
    kStart = s
    visited = []
    curr = Queue()
    curr.put(kStart)
    while not curr.empty():
        node = curr.get()
        
        #algo might revisit duplicates in curr
        if node in visited:
            continue
        
        visited.append(node)
        for entry in m[node]:
            if entry not in visited:
                curr.put(entry)
    return visited

def count(m):
    visited = []
    count = 0
    while len(visited) < len(m):
        for i in range(len(m)):
            if i not in visited:
                n=i
                break
        new = bfs(m, n)
        for i in new:
            visited.append(i)
        count += 1
    return count    

def main():
    m = initr()
    print(count(m))

main()
