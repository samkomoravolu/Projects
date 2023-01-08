from queue import Queue

inf = 2147483647

def initr():
    m=[[0],[2], [1]]
    return m

def chromaticSub(m, s):
    colors = [-1 for i in range(len(m))]
    num = 0
    curr = Queue(); curr.put(s)
    visited = []
    while not curr.empty():
        node = curr.get()
        if node in visited:
            continue

        surrounding = []
        
        visited.append(node)
        for i in m[node]:
            surrounding.append(colors[i])
            if i not in visited:
                curr.put(i)
        

        c = 1
        while c in surrounding:
            c += 1
        colors[node] = c
        if c > num:
            num = c
    return num, visited

def chromaticNumber(m):
    visited = []
    c = 0
    while len(visited) < len(m):
        for i in range(len(m)):
            if i not in visited:
                n = i
                break
        new = chromaticSub(m, n)
        if c < new[0]:
            c = new[0]
        for i in new[1]:
            if i not in visited:
                visited.append(i)
    return c

def main():
    m = initr()
    print(chromaticNumber(m))

main()
