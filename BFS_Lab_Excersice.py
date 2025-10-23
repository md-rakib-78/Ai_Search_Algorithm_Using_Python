import random
def pathFind(par, i, j, m, n):
    if (i == m and j == n):
        print("(", m,",",n, ") -> ", end="")
    else:
        lst = par[m][n]
        pathFind(par, i, j, lst[0], lst[1])
        print("(", m, ",", n, ") -> ", end="")

def BFS(graph, sX, sY, gX, gY, N):
    queue = []
    visit = []
    pNode = []
    for v in range(N):
        row = []
        pow = []
        for u in range(N):
            row.append("w")
            pow.append(0)
        visit.append(row)
        pNode.append(pow)

    visit[sX][sY] = "g"
    lst = [sX, sY]
    queue.append(lst)
    while queue:
        curr = queue.pop(0)
        x = curr[0]
        y = curr[1]

        #print("Current Position: ",x," , ",y)
        # check goal
        if x == gX and y == gY:
            print("Goal found at -> (", x, ",", y, ")")
            print("Start State To Goal State Path: ")
            pathFind(pNode, sX, sY, gX, gY)
            print()
            return

        # Right
        if y + 1 < N and graph[x][y + 1] == 1 and visit[x][y + 1] == "w":
            #print("Moving Right -> (", x, ",", y + 1, ")")
            pNode[x][y + 1] = curr
            visit[x][y + 1] = "g"
            queue.append([x, y + 1])


        # Left
        if y - 1 >= 0 and graph[x][y - 1] == 1 and visit[x][y - 1] == "w":
            #print("Moving Left -> (", x, ",", y - 1, ")")
            pNode[x][y - 1] = curr
            visit[x][y - 1] = "g"
            queue.append([x, y - 1])


        # Down
        if x + 1 < N and graph[x + 1][y] == 1 and visit[x + 1][y] == "w":
            #print("Moving Down -> (", x + 1, ",", y, ")")
            pNode[x + 1][y] = curr
            visit[x + 1][y] = "g"
            queue.append([x + 1, y])


        # Up
        if x - 1 >= 0 and graph[x - 1][y] == 1 and visit[x - 1][y] == "w":
            #print("Moving Up -> (", x - 1, ",", y, ")")
            pNode[x - 1][y] = curr
            visit[x - 1][y] = "g"
            queue.append([x - 1, y])

        visit[x][y] = "B"

    print("Goal not reachable.")



matrix = []


with open("example.txt", "r") as file:
    for line in file:
        row = list(map(int ,line.strip().split()))
        matrix.append(row)

n = len(matrix)
print("----Matrix----")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

startX, startY = map(int, input("Enter the start position x & y: ").split())
goalX, goalY = map(int, input("Enter the goal position x & y: ").split())

BFS(matrix, startX, startY, goalX, goalY, n)
