prev = []
visit = []
adjacent = []
color = []
colorNode = []
CountryState=[]
count=0

def DFS_Visit(adjacent, curr, n):
    global count
    visit[curr] = "g"

    used_colors = set()
    for neigh in adjacent[curr]:
        if colorNode[neigh] is not None:
            used_colors.add(colorNode[neigh])

    for c in color:
        if c not in used_colors:
            colorNode[curr] = c
            count=count+1
            break

    # Visit neighbors
    for v in adjacent[curr]:
        if visit[v] == "w":
            prev[v] = curr
            DFS_Visit(adjacent, v, n)

    visit[curr] = "b"


def DFS(adjacent):
    global prev, visit, color, colorNode,countn,CountryState

    n = len(adjacent)
    prev = [-1] * n
    visit = ["w"] * n

    color = ["red", "green", "blue", "yellow", "gray", "brown"]

    colorNode = [None] * n

    # Run DFS from every unvisited node (handles disconnected graphs)
    for u in range(n):
        if visit[u] == "w":
            DFS_Visit(adjacent, u, n)

    print("\n--Country State Colors--")
    for i in range(len(colorNode)):
        print(f"{CountryState[i]} -> {colorNode[i]}")


# ---- MAIN ----
matrix = []
with open("lab_task_graph_coloring_matrix.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        row = list(map(int, line.split()))
        matrix.append(row)

n = len(matrix)
CountryState = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
adjacent = [[] for _ in range(n)]

for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            if j not in adjacent[i]:
                adjacent[i].append(j)
            if i not in adjacent[j]:
                adjacent[j].append(i)
print()
print("--County state short form--")
print("1. Western Australia = WA")
print("2. Northern Territory = NT")
print("3. South Australia = SA")
print("4. Queensland = Q")
print("5. New South Wales = NSW")
print("6. Victoria = V")
print("7. Tasmania = T")
print()

print("--Adjacent States--")
for i in range(len(adjacent)):
    print(CountryState[i], "--> ", end="")
    for j in range(len(adjacent[i])):
        print(CountryState[adjacent[i][j]], " | ", end="")
    print()

DFS(adjacent)
