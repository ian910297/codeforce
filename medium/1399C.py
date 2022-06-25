import sys
from heapq import heappush
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

def find_pair(nums, left, right):
    global used

    if right - left == 0:
        return 0

    tmp = {}
    while left < right:
        tag = '{}_{}'.format(nums[left], nums[right])
        s = nums[left] + nums[right]
        if s in tmp and tag in tmp[s]:
            tmp[s][tag] += 1
        elif s in tmp and tag not in tmp[s]:
            tmp[s][tag] = 1
        else:
            tmp[s] = {}
            tmp[s][tag] = 1

        left += 1
        right -= 1
    
    # copy back to global used
    for key in tmp:
        if key not in used:
            used[key] = {}
        for tag in tmp[key]:
            if tag not in used[key]:
                used[key][tag] = tmp[key][tag]
            else:
                used[key][tag] = max(used[key][tag], tmp[key][tag])
T = int(input())
for _ in range(T):
    __ = sys.stdin.readline()
    data = get_ints()
    data = sorted(data)

    ans = 0
    used = {}
    for i in range(len(data)):
        for j in range(len(data)-1, i-1, -1):
            if i < j:
                find_pair(data, i, j)
    
    for key in used:
        count = 0
        for tag in used[key]:
            count += used[key][tag]
        ans = max(ans, count)
    # print(used)
    print(ans)