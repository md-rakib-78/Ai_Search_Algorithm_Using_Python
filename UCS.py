
def pathfind(graph,prev,s,e):
    if(s==e):
        print(e," ", end="")
        return
    else:
        pathfind(graph,prev,s,prev[e])
        print(e," ", end="")

def UCS(graph,st,en):

    prev=[-1]*len(graph)
    visit=["w"]*len(graph)
    track=[0]*len(graph)

    prev[st]=-1
    visit[st]="g"
    queue=[]
    queue.append(st)
    print()
    print("UCS Expand: ", end="")
    while queue:
        list=[]
        list=queue
        list.sort()
        queue=list
        s=queue.pop(0)
        print(s," ", end="")

        for i in range(len(graph)):
            if visit[i]!="b" and graph[s][i]>0:
                x=track[s]+graph[s][i]
                if x<track[i] or track[i]==0:
                    track[i]=x
                    visit[i]="b"
                    prev[i]=s
                    queue.append(i)

        visit[s]="b"

    print()
    print("Shortest path:-> ", end=" ")
    pathfind(graph,prev,st,en)


graph=[]
with open("rtp.txt", "r") as file:
    for line in file:
        row=list(map(int, line.strip().split()))
        graph.append(row)

st=int(input("Enter the start state: "))
en=int(input("Enter the goal State: "))

print("---Adjency Matrix---")
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j],end=" ")
    print()

UCS(graph,st,en)


