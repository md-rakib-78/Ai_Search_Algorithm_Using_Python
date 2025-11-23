prev = []
visit = []
sumi = []
lst = []

def pathfinding(start, goal):
    if start == goal:
        print(goal," ",end="")
        return
    else:
        pathfinding(start,prev[goal])
        print(goal," ",end="")
        return


def function(addition, h, node):
    return addition + h[node]


def checklist(v,fval):
    for i in range(len(lst)):
        if lst[i][1]==v:
            if lst[i][0]<fval:
                return
            else:
                lst.pop(i)
                list.append([fval,v])
                return
    lst.append([fval, v])


def DFS_Visit(graph, curr, n, en, h):

    visit[curr] = "b"

    # Expand neighbors
    for v in range(n):
        if visit[v] != "b" and graph[curr][v] != 0:
            prev[v] = curr
            sumi[v] = sumi[curr] + graph[curr][v]
            f_val = function(sumi[v], h, v)
            checklist(v,f_val)


    if not lst:
        return

    lst.sort()
    print(lst)
    next_node = lst.pop(0)[1]
    print("Curr Node: ",next_node)
    DFS_Visit(graph, next_node, n, en, h)


def DFS(graph, st, en, h):
    global prev, visit, sumi, lst
    prev = [-1] * len(graph)
    visit = ["w"] * len(graph)
    sumi = [0] * len(graph)  # initialize g(n)
    lst = []  # open list empty at start

    DFS_Visit(graph, st, len(graph), en, h)
    print()
    pathfinding(st, en)


# Read matrix
matrix=[]

#user Input Matrix
for i in range(5):
     mat=[]
     mat= list(map(int,input().split()))
     matrix.append(mat)

s = int(input("Enter the Source Node: "))
e = int(input("Enter the Goal Node: "))
h = [2, 4, 1, 1, 0]  # heuristic values
print()
DFS(matrix, s, e, h)
