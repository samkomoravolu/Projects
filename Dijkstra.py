from queue import Queue

inf = 2147483647

def initr():
    m=[[1,2,3,4],[2,3,8],[0,1,4],[0,2,3],[1,3],[5,6],[5,6],[7],[9],[11],[10],[10]]
    return m

def shortestPath(m, n1, n2):
    unvisited = [i for i in range(len(m))]
    distances = [inf for i in range(len(m))]
    distances[n1] = 0
    curr = Queue()
    curr.put(n1)
    while n2 in unvisited and not curr.empty():
        node = curr.get()
        if node not in unvisited:
            continue
        unvisited.remove(node)
        for i in m[node]:
            if i in unvisited:
                curr.put(i)
                d = distances[node] + 1
                if d < distances[i]:
                    distances[i] = d
    return distances[n2]

def main():
    m = initr()
    d = shortestPath(m, 10, 3)
    if d == inf:
        print("Node unreachable")
    else:
        print(d)

main()
