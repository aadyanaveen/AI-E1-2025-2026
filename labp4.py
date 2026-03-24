import heapq

GOAL_STATE = [[1,2,3],[4,5,6],[7,8,0]]

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.get_blank_position()

        moves = {
            "Up": (x-1, y),
            "Down": (x+1, y),
            "Left": (x, y-1),
            "Right": (x, y+1)
        }

        for move_name, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]
                
                # Swap blank with adjacent tile
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                
                successors.append(Puzzle(new_state, self, move_name, self.depth + 1))
        
        return successors


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def astar(initial_state):
    start = Puzzle(initial_state)
    pq = []
    
    counter = 0  # tie-breaker
    heapq.heappush(pq, (heuristic(start.state), counter, start))
    
    visited = set()

    while pq:
        _, _, current = heapq.heappop(pq)

        if current.is_goal():
            return current

        visited.add(str(current.state))

        for neighbor in current.generate_successors():
            if str(neighbor.state) not in visited:
                cost = neighbor.depth + heuristic(neighbor.state)
                counter += 1
                heapq.heappush(pq, (cost, counter, neighbor))
    
    return None


def print_solution(goal_node):
    path = []
    while goal_node:
        path.append(goal_node)
        goal_node = goal_node.parent
    
    path.reverse()

    print("\nSolution Steps:\n")
    for i, node in enumerate(path):
        if i == 0:
            print(f"Step {i}: Initial State")
        else:
            print(f"Step {i}: Move {node.move}")
        node.display()


# ------------------ Main ------------------

print("Enter initial state (3x3 puzzle, use 0 for blank):")

initial_state = []
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    initial_state.append(row)

result = astar(initial_state)

if result:
    print_solution(result)
else:
    print("No solution found.")