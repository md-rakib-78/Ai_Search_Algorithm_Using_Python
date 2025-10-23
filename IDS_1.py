prev = []
visit = []
goalReach = False

def pathFind(i, j):
    if i == j:
        print(j, end=" ")
        return
    else:
        pathFind(i, prev[j])
        print(j, end=" ")

def DFS_Visit(graph, goal, curr, depth, limit, n):
    global goalReach
    visit[curr] = "g"
    print(curr, end=" ")

    if goal == curr:
        goalReach = True
        return

    if depth == limit:
        visit[curr] = "b"
        return

    for v in range(n):
        if visit[v] == "w" and graph[curr][v] == 1:
            prev[v] = curr
            DFS_Visit(graph, goal, v, depth + 1, limit, n)

    visit[curr] = "b"

def DFS(graph, st, en, limit):
    global prev, visit, goalReach
    prev = [-1] * len(graph)
    visit = ["w"] * len(graph)
    goalReach = False

    DFS_Visit(graph, en, st, 0, limit, len(graph))



matrix = []
with open("example.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
limit = 1
print()

i = 0
while True:
    print("Iterative:", i)
    DFS(matrix, s, e, i)

    if goalReach == False:
        print()
        print("No Goal Reach increment limit!")
        i += 1
    else:
        print()
        print("Goal Reach!")
        print("Path from", s, "to", e, "--> ", end="")
        pathFind(s, e)
        print()
        break
    print()
