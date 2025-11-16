prev = []
visit = []
time = 0
lt = []
lst = []
found = False

def DFS(graph, curr, goal, limit, depth, n):
    global time, lst, found
    time += 1
    print(curr, " ", end="")

    visit[curr] = "g"

    if curr == goal:
        found = True

    if depth == limit:
        visit[curr] = "b"
        time += 1
        lt = [time, curr]
        lst.append(lt)
        return

    for v in range(n - 1, -1, -1):
        if graph[curr][v] == 1 and visit[v] == "w":
            prev[v] = curr
            DFS(graph, v, goal, limit, depth + 1, n)

    if visit[curr] != "b":
        visit[curr] = "b"
        time += 1
        lt = [time, curr]
        lst.append(lt)
    return

def IDS(graph, st, en, max_limit):
    n = len(graph)
    global prev, visit, lt, lst, time, found

    for limit in range(max_limit + 1):
        prev = [-1] * n
        visit = ["w"] * n
        lst = []
        time = 0
        found = False

        print("Iterative Depth:", limit)
        print("DFS:", end=" ")

        DFS(graph, st, en, limit, 0, n)

        print()
        if found:
            print("Goal found!\n")
            print("\n")
        else:
            print("Goal not found at this depth.\n")

        print("Topological Order: ", end="")
        lst.sort(reverse=True)
        for l in lst:
            print(" ", l[1], end=" ")
        print("\n")

        if found:
            return

    print("Goal not found in given depth limit.")

matrix = []
with open("Direct Graph Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

print("Direct Graph matrix: ")
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print()
s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
max_limit = int(input("Enter the Max Depth Limit: "))
print()
IDS(matrix, s, e, max_limit)
