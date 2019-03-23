# python3

import sys

n, m = map(int, sys.stdin.readline().split())
rank = list(map(int, sys.stdin.readline().split()))
parent = list(range(n))
ans = max(rank)

def get_parent(table):
    while parent[table] != table:
        parent[table] = parent[parent[table]]
        table = parent[table]
    return parent[table]


def merge(destination, source):
    temp_size = -1000000000000
    global ans
    root_destination, root_source = get_parent(destination), get_parent(source)

    if root_destination == root_source:
        return False
    if rank[root_source] <= rank[root_destination]:
        parent[root_source] = root_destination
        rank[root_destination] += rank[root_source]
        rank[root_source] = 0
        temp_size = rank[root_destination]
    else:
        parent[root_destination] = root_source
        rank[root_source] += rank[root_destination]
        rank[root_destination] = 0
        temp_size = rank[root_source]
    if temp_size > ans:
        ans = temp_size
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)