prev = []
visit = []
i=0
j=0



def DFS_Visit(graph, curr, n):

    if graph[][]==





def DFS(graph):
    global visit,i,j
    visit = ["w"] * len(graph)
    DFS_Visit(graph, 0, len(graph))


matrix = []
numQueen=int(input("Enter the number of Queens: "))
for i in range(numQueen):
    lst=[]
    for j in range(numQueen):
        lst.append(0)
    matrix.append(lst)

print(matrix)

print()
DFS(matrix)
