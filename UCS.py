count=0
def pathfind(graph,prev,s,e):
    global count
    if(s==e):
        print(e," ", end="")
        return
    else:
        count+=graph[e][prev[e]]
        pathfind(graph,prev,s,prev[e])
        print(e," ", end="")

def UCS(graph,st,en):

    prev=[-1]*len(graph)
    visit=["w"]*len(graph)
    track=[0]*len(graph)

    prev[st]=-1
    visit[st]="g"
    queue = []
    queue.append([0, st])
    print()
    print("UCS Expand: ", end="")

    while queue:
        queue.sort()
        s = queue.pop(0)
        print(s[1], " ", end="")

        for i in range(len(graph)):
            if visit[i] != "b" and graph[s[1]][i] > 0:
                x = track[s[1]] + graph[s[1]][i]
                if x < track[i] or track[i] == 0:
                    lst = [x, i]
                    track[i] = x
                    visit[i] = "b"
                    prev[i] = s[1]
                    queue.append(lst)

        visit[s[1]] = "b"

    print()
    print("Shortest path:-> ", end=" ")
    pathfind(graph,prev,st,en)
    print()
    print("Total Path Cost: ", count)


graph=[]
with open("Matrix For UCS.txt", "r") as file:
    for line in file:
        row=list(map(int, line.strip().split()))
        graph.append(row)

st=int(input("Enter the start state: "))
en=int(input("Enter the goal State: "))
print()
print("---Adjency Matrix---")
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j],end=" ")
    print()

UCS(graph,st,en)


