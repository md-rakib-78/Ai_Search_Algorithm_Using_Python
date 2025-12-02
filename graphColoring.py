prev = []
visit = []
color = []
track = []

def DFS_Visit(graph, curr, n):
    visit[curr] = "g"

    print(f"Node {curr} Color = {track[curr]}")

    for v in range(n):
        if graph[curr][v] == 1 and visit[v] == "w":

            for i in range(len(color)):
                if color[i] != track[curr]:
                    track[v] = color[i]

            DFS_Visit(graph, v, n)

    visit[curr] = "b"

def DFS(graph):
    global prev, visit, color, track

    n = len(graph)
    prev = [-1] * n
    visit = ["w"] * n
    color = ["red", "green", "blue"]

    track.clear()
    track.extend([None] * n)


    track[0] = color[0]

    DFS_Visit(graph, 0, n)
    print()

# ---- MAIN ----
matrix = []
with open("graph matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

DFS(matrix)
