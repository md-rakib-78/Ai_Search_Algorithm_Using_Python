prev = []
visit = []
i = 0
j = 0


def DFS_Visit(graph):
    global i, j

    N = len(graph)

    if i == N:
        return True

    if j == N:
        return False

    graph[i][j] = 1

    for row in range(i - 1, -1, -1):
        if graph[row][j] == 1:
            graph[i][j] = 0
            j += 1
            return DFS_Visit(graph)

    for d in range(1, min(i, j) + 1):
        if graph[i - d][j - d] == 1:
            graph[i][j] = 0
            j += 1
            return DFS_Visit(graph)

    for d in range(1, min(i, N - j - 1) + 1):
        if graph[i - d][j + d] == 1:
            graph[i][j] = 0
            j += 1
            return DFS_Visit(graph)


    ni = i + 1
    nj = 0


    old_i, old_j = i, j

    i, j = ni, nj
    if DFS_Visit(graph):
        return True

    i, j = old_i, old_j
    graph[i][j] = 0
    j += 1
    return DFS_Visit(graph)



def DFS(graph):
    global visit, i, j
    visit = ["w"] * len(graph)
    i = 0
    j = 0
    DFS_Visit(graph)



matrix = []
numQueen = int(input("Enter number of Queens: "))

for i in range(numQueen):
    lst = []
    for j in range(numQueen):
        lst.append(0)
    matrix.append(lst)

DFS(matrix)

print("\nFinal N-Queen Solution:")
for r in matrix:
    print(r)
