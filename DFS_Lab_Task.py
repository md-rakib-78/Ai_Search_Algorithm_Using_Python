import random

def pathFind(par, i, j, m, n):
    if (i == m and j == n):
        print("(", m,",",n, ") -> ", end="")
    else:
        lst = par[m][n]
        pathFind(par, i, j, lst[0], lst[1])
        print("(", m, ",", n, ") -> ", end="")


def DFS(graph, sX, sY, gX, gY, N):
    stack = []
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
    stack.append(lst)

    while stack:
        curr = stack.pop(0)
        x = curr[0]
        y = curr[1]

        print("Current Position: ",x," , ",y)
        # check goal
        if x == gX and y == gY:
            print("Goal found at -> (", x, ",", y, ")")
            print()
            print("Path :-> ")
            pathFind(pNode,sX,sY,gX,gY)
            return

        # Right
        if y + 1 < N and graph[x][y + 1] == 1 and visit[x][y + 1] == "w":
            print("Moving Right -> (", x, ",", y + 1, ")")
            pNode[x][y + 1] = curr
            visit[x][y + 1] = "g"
            stack.insert(0,[x, y + 1])

        # Left
        if y - 1 >= 0 and graph[x][y - 1] == 1 and visit[x][y - 1] == "w":
            print("Moving Left -> (", x, ",", y - 1, ")")
            pNode[x][y - 1] = curr
            visit[x][y - 1] = "g"
            stack.insert(0,[x, y - 1])


        # Down
        if x + 1 < N and graph[x + 1][y] == 1 and visit[x + 1][y] == "w":
            print("Moving Down -> (", x + 1, ",", y, ")")
            pNode[x + 1][y] = curr
            visit[x + 1][y] = "g"
            stack.insert(0,[x + 1, y])

        # Up
        if x - 1 >= 0 and graph[x - 1][y] == 1 and visit[x - 1][y] == "w":
            print("Moving Up -> (", x - 1, ",", y, ")")
            pNode[x - 1][y] = curr
            visit[x - 1][y] = "g"
            stack.insert(0,[x - 1, y])

        visit[x][y] = "B"
    print("Goal not reachable.")


matrix=[]
n=int(input("Enter the grid size: "))

for i in range(n):
    row=[]
    for j in range(n):
        ran=random.randint(0,1)
        row.append(ran)
    matrix.append(row)

print()
print("---- Matrix ----")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

startX, startY = map(int, input("Enter the start position x & y: ").split())
goalX, goalY = map(int, input("Enter the goal position x & y: ").split())

DFS(matrix, startX, startY, goalX, goalY, n)
