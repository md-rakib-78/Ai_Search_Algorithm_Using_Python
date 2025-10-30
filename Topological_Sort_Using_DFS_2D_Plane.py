prev = []
visit = []
d = []
f = []
lst=[]
time = 0

def DFS_Visit(graph, curr, n):
    global time
    visit[curr] = "g"
    time += 1
    d[curr] = time

    for v in range(n):
        if visit[v] == "w" and graph[curr][v] == 1:
            prev[v] = curr
            DFS_Visit(graph, v, n)

    visit[curr] = "b"
    time += 1
    f[curr] = time
    lt=[]
    lt=[time,curr]
    lst.append(lt)


def DFS(graph):
    global prev, visit, d, f, time,lst
    prev = [-1] * len(graph)
    visit = ["w"] * len(graph)
    d = [0] * len(graph)
    f = [0] * len(graph)
    time = 0

    for i in range(len(graph)):
        if visit[i] == "w":
            DFS_Visit(graph, i, len(graph))

    print()
    print("Topological Order of Robot Node Traversal: ")
    lst.sort(reverse=True)
    for l in lst:
        print(" ", l[1],end=" ")

    print()

matrix = []
with open("Direct Graph Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

print()
print("---- Matrix ----")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print()
DFS(matrix)
