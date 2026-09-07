def DFS(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(len(graph)):
        if graph[vertex][i] == 1 and visited[i] == False:
            DFS(graph, i, visited)


def BFS(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for i in range(len(graph)):
            if graph[vertex][i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append(i)


n = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertex: "))

visited = [False] * n

print("\nDFS Traversal:")
DFS(graph, start, visited)

print("\nBFS Traversal:")
BFS(graph, start)

print("\nEN.No:92460118673")
