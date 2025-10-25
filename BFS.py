def pathFind(par,i,j):
    if(i==j):
        print(j)
        return
    else:
        pathFind(par,i,par[j])
        print(j)

def BFS(graph, start, end):
    queue = []
    visit = ["W"] * len(graph)
    level = [-1] * len(graph)
    pNode = [-1] * len(graph)


    visit[start] = "G"
    level[start] = 0
    queue.append(start)

    while queue:
        curr = queue.pop(0)
        print(curr, end=" ")

        for j in range(len(graph)):
            if graph[curr][j] == 1 and visit[j] == "W":
                visit[j] = "G"
                level[j] = level[curr] + 1
                pNode[j] = curr
                queue.append(j)

        visit[curr] = "B"  # mark current node fully visited


    print("\nParent nodes:", pNode)
    print("Levels:", level)
    with open("exp.txt",'a') as f:
        f.write(str(level[3]) + "\n")

    pathFind(pNode,start,end)

matrix = []
with open("Tree Matrix.txt", "r") as file:
    for line in file:
        row = list(map(int ,line.strip().split()))
        matrix.append(row)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
print()
BFS(matrix, s, e)
