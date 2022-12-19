#DALILA BESSEGHIR 
# Kamelia Brahimi

from collections import Counter, defaultdict

#https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem
MOD = 10**9 + 7

def read_row():
    return (int(x) for x in input().split())

def mul(x, y):
    return (x * y) % MOD

def add(*args):
    return sum(args) % MOD

def sub(x, y):
    return (x - y) % MOD

n, q = read_row()

# Construct adjacency list of the tree
adj_list = defaultdict(list)

for _ in range(n - 1):
    u, v = read_row()
    adj_list[u].append(v)
    adj_list[v].append(u)

# Construct element to set mapping {element: [sets it belongs to]}
elements = {v: set() for v in adj_list}

for set_no in range(q):
    read_row()
    for x in read_row():
        elements[x].add(set_no)

# Do BFS to find parent for each node and order them in reverse depth
root = next(iter(adj_list))
current = [root]
current_depth = 0
order = []
parent = {root: None}
depth = {root: current_depth}

while current:
    current_depth += 1
    order.extend(current)
    nxt = []
    for node in current:
        for neighbor in adj_list[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                depth[neighbor] = current_depth
                nxt.append(neighbor)

    current = nxt

# Process nodes in the order created above
score = Counter()
# {node: {set_a: [depth, sum of nodes, flow]}}
state = {}
for node in reversed(order):
    states = [state[neighbor] for neighbor in adj_list[node] if neighbor != parent[node]]
    largest = {s: [depth[node], node, 0] for s in elements[node]}

    if states:
        max_index = max(range(len(states)), key=lambda x: len(states[x]))
        if len(states[max_index]) > len(largest):
            states[max_index], largest = largest, states[max_index]


    sets = defaultdict(list)
    for cur_state in states:
        for set_no, v in cur_state.items():
            sets[set_no].append(v)

    for set_no, states in sets.items():
        if len(states) == 1 and set_no not in largest:
            largest[set_no] = states[0]
            continue

        if set_no in largest:
            states.append(largest.pop(set_no))

        total_flow = 0
        total_node_sum = 0

        for node_depth, node_sum, node_flow in states:
            flow_delta = mul(node_depth - depth[node], node_sum)
            total_flow = add(total_flow, flow_delta, node_flow)
            total_node_sum += node_sum

        set_score = 0

        for node_depth, node_sum, node_flow in states:
            node_flow = add(mul(node_depth - depth[node], node_sum), node_flow)
            diff = mul(sub(total_flow, node_flow), node_sum)
            set_score = add(set_score, diff)

        score[set_no] = add(score[set_no], set_score)
        largest[set_no] = (depth[node], total_node_sum, total_flow)

    state[node] = largest

print(*(score[i] for i in range(q)), sep='\n')