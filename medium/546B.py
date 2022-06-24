import sys
from heapq import heappush
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


T = int(input())
# for _ in range(T):
# parser
# N, M = get_ints()
data = get_ints()
data = sorted(data)
cost = 0
visited = {}
db = []
for num in data:
    if num not in visited:
        visited[num] = 1
        heappush(db, num)
    else:
        be_paid = db[-1] + 1 - num
        cost += be_paid
        heappush(db, num + be_paid)
        visited[db[-1]] = 1
print(cost)
        