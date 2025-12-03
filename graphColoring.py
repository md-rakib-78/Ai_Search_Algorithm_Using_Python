prev = []
visit = []
adjacent = []
color = []
colorNode = []
count=0

def DFS_Visit(adjacent, curr, n):
    """Recursive DFS visit that colors `curr` using colors not used by its neighbors."""
    global count
    visit[curr] = "g"

    # Determine colors used by *all* adjacent nodes (undirected adjacency)
    used_colors = set()
    for neigh in adjacent[curr]:
        if colorNode[neigh] is not None:
            used_colors.add(colorNode[neigh])

    print(used_colors)
    # Pick first available color
    for c in color:
        if c not in used_colors:
            colorNode[curr] = c
            count+=1
            break

    # Visit neighbors
    for v in adjacent[curr]:
        if visit[v] == "w":
            prev[v] = curr
            DFS_Visit(adjacent, v, n)

    visit[curr] = "b"


def DFS(adjacent):
    global prev, visit, color, colorNode,count

    n = len(adjacent)
    prev = [-1] * n
    visit = ["w"] * n

    # color palette (add more if needed)
    color = ["red", "green", "blue", "yellow", "gray", "brown"]

    colorNode = [None] * n

    # Run DFS from every unvisited node (handles disconnected graphs)
    for u in range(n):
        if visit[u] == "w":
            DFS_Visit(adjacent, u, n)

    print("\nNode Colors:")
    for i in range(len(colorNode)):
        print(f"Node {i} -> {colorNode[i]}")

    print("Total color needed: ",count)


# ---- MAIN ----
matrix = []
with open("graph coloring matrix.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        row = list(map(int, line.split()))
        matrix.append(row)

n = len(matrix)
# initialize adjacency lists
adjacent = [[] for _ in range(n)]

# Build undirected adjacency: for every edge i->j, add j to i and i to j.
for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            if j not in adjacent[i]:
                adjacent[i].append(j)
            if i not in adjacent[j]:
                adjacent[j].append(i)

# Print adjacency
for i in range(len(adjacent)):
    print(i, "->", end="")
    for j in range(len(adjacent[i])):
        print(adjacent[i][j], " ", end="")
    print()

DFS(adjacent)
