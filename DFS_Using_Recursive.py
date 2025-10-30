prev = []
visit = []
d = []
f = []
time = 0 

def pathFind(i, j):
    if i == j:
        print(j, end=" ")
        return
    else:
        pathFind(i, prev[j])
        print(j, end=" ")

def DFS_Visit(graph, curr, n):
    global time
    visit[curr] = "g"
    time += 1
    d[curr] = time 
    
    print(curr, end=" ")
    
    for v in range(n):
        if visit[v] == "w" and graph[curr][v] == 1:
            prev[v] = curr
            DFS_Visit(graph, v, n)
    
    visit[curr] = "b"
    time += 1
    f[curr] = time  

def DFS(graph, st, en):
    global prev, visit, d, f, time
    prev = [-1] * len(graph)
    visit = ["w"] * len(graph)
    d = [0] * len(graph)
    f = [0] * len(graph)
    time = 0
    
    for i in range(len(graph)):
        if visit[i] == "w":
            DFS_Visit(graph, i, len(graph))
    
    print("\nParent Nodes:")
    print(prev)
    
    print("Discovery Times:")
    print(d)
    
    print("Finish Times:")
    print(f)
    
    print("Path from", st, "to", en, ":")
    pathFind(st, en)
    print()


matrix = []
with open("Tree Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
print()
DFS(matrix, s, e)
