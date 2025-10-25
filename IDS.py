prev = []
visit = []

def pathFind(i, j):
    if i == j:
        print(j, end=" ")
        return
    else:
        pathFind(i, prev[j])
        print(j, end=" ")

def DLS(graph, curr, goal, limit, depth, n):
    if curr == goal:
        return True

    if depth == limit:
        return False

    visit[curr] = "g"
    for v in range(n):
        if graph[curr][v] == 1 and visit[v] == "w":
            prev[v] = curr
            if DLS(graph, v, goal, limit, depth + 1, n):
                return True
    visit[curr] = "b"
    return False

def IDS(graph, st, en, max_limit):
    n = len(graph)
    for limit in range(max_limit + 1):
        global prev, visit
        prev = [-1] * n
        visit = ["w"] * n
        print(f"Iterative Depth: {limit}")
        if DLS(graph, st, en, limit, 0, n):
            print("Goal found!")
            print("Path:", end=" ")
            pathFind(st, en)
            print("\n")
            return
        else:
            print("Goal not found at this depth.\n")

    print("Goal not found in given depth limit.")


matrix = []
with open("Tree Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
max_limit = int(input("Enter the Max Depth Limit: "))

IDS(matrix, s, e, max_limit)
