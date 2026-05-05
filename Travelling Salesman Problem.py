# Travelling Salesman Problem using Nearest Neighbor Heuristic

def tsp_nearest_neighbor(graph, start):
    n = len(graph)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total_cost = 0
    current = start

    for _ in range(n - 1):
        nearest = -1
        min_cost = float('inf')

        # Find nearest unvisited city
        for city in range(n):
            if not visited[city] and graph[current][city] < min_cost:
                min_cost = graph[current][city]
                nearest = city

        # Move to nearest city
        path.append(nearest)
        visited[nearest] = True
        total_cost += min_cost
        current = nearest

    # Return to starting city
    total_cost += graph[current][start]
    path.append(start)

    return path, total_cost


# User input
n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting city (0 to n-1): "))

path, cost = tsp_nearest_neighbor(graph, start)

print("\nPath followed:", " -> ".join(map(str, path)))
print("Total cost:", cost)