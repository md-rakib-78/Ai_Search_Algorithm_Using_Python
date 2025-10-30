prev = []
visit = []
lst = []
time = 0

def DFS(graph, curr, goal, limit, depth, n):
    global time, lst
    time += 1
    print(curr, " ", end="")

    if curr == goal:
        return True

    if depth == limit:
        return False

    visit[curr] = "g"
    for v in range(n):
        if graph[curr][v] == 1 and visit[v] == "w":
            prev[v] = curr
            DFS(graph, v, goal, limit, depth + 1, n)
    visit[curr] = "b"
    time += 1
    lt = [time, curr]
    lst.append(lt)
    return False


def IDS(graph, st, en, max_limit):
    n = len(graph)
    global prev, visit, lst, time

    for limit in range(max_limit + 1):
        prev = [-1] * n
        visit = ["w"] * n
        lst = []
        time = 0

        print("Iterative Depth:", limit)
        print("DFS:", end=" ")

        if DFS(graph, st, en, limit, 0, n):
            print("\nGoal found!\n")
            print("Topological Order of Robot Node Traversal:")
            lst.sort(reverse=True)
            for l in lst:
                print(" ", l[1], end=" ")
            print()
            return
        else:
            print("\nGoal not found at this depth.\n")

    print("Goal not found in given depth limit.")


matrix = []
with open("Direct Graph Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
max_limit = int(input("Enter the Max Depth Limit: "))

IDS(matrix, s, e, max_limit)
