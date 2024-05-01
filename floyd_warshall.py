INF= float('inf')

def floyd_warshall(graph):
    V=len(graph)
    dist=[[0] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            dist[i][j]=graph[i][j]
            
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
                        
    return dist 

graph=[
    [0,3,1,0],
    [3,0,1,INF],
    [1,1,0,1],
    [3,INF,1,0]
]       

all_pair_shortest_path = floyd_warshall(graph)
print("ALL PAIR SHORTEST PATH:")
for row in all_pair_shortest_path:
    print(row)            