visit=[]
prev=[]

def DFS(graph, st,en):
    global visit,prev
    visit=["w"]*len(graph)
    prev=[-1]*len(graph)

    stack=[st]
    visit[st]="g"

    while stack:
        print("Stack:-> ",stack)
        curr=stack.pop(0)
        print("DFS:-> ",curr)

        for i in range(len(graph)-1,-1,-1):
            if graph[curr][i]==1 and visit[i]=="w":
                stack.insert(0,i)
                visit[i]="g"
                prev[i]=curr

        visit[curr]="b"


matrix=[]
with open("Tree Matrix.txt", "r") as f:
    for line in f:
        row=list(map(int, line.split()))
        matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print()
start=int(input("Enter the start node: "))
end=int(input("Enter the end node: "))
print()
DFS(matrix,start,end)
