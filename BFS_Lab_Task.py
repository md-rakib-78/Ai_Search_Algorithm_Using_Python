import random

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
    count=0
    while queue:
        curr = queue.pop(0)
        x = curr[0]
        y = curr[1]

        print("Current Position: ",x," , ",y)
        # check goal
        if x == gX and y == gY:
            print("Goal found at -> (", x, ",", y, ")")
            return

        # Right
        if y + 1 < N and graph[x][y + 1] == 1 and visit[x][y + 1] == "w":
            print("Moving Right -> (", x, ",", y + 1, ")")
            pNode[x][y + 1] = curr
            visit[x][y + 1] = "g"
            queue.append([x, y + 1])

        # Left
        if y - 1 >= 0 and graph[x][y - 1] == 1 and visit[x][y - 1] == "w":
            print("Moving Left -> (", x, ",", y - 1, ")")
            pNode[x][y - 1] = curr
            visit[x][y - 1] = "g"
            queue.append([x, y - 1])


        # Down
        if x + 1 < N and graph[x + 1][y] == 1 and visit[x + 1][y] == "w":
            print("Moving Down -> (", x + 1, ",", y, ")")
            pNode[x + 1][y] = curr
            visit[x + 1][y] = "g"
            queue.append([x + 1, y])

        # Up
        if x - 1 >= 0 and graph[x - 1][y] == 1 and visit[x - 1][y] == "w":
            print("Moving Up -> (", x - 1, ",", y, ")")
            pNode[x - 1][y] = curr
            visit[x - 1][y] = "g"
            queue.append([x - 1, y])


        count+=1

        visit[x][y] = "B"

    print("Goal not reachable.")


matrix = []

n = int(input("Enter the grid size: "))
obs = int(n * n)
print("Total obstacles:", obs)

for i in range(n):
    lst = []
    for j in range(n):
        lst.append(random.randint(0, 1))
    matrix.append(lst)

print("----Matrix----")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


startX, startY = map(int, input("Enter the start position x & y: ").split())
goalX, goalY = map(int, input("Enter the goal position x & y: ").split())

BFS(matrix, startX, startY, goalX, goalY, n)
