def find_largest(l, r, mid):
    if l > mid:
        return find_largest(l, r, (mid + r)//2)
    else:
        answer = r % mid
        if answer == 0:
            answer = (r-1) % mid

        return answer

def main():
    times = eval(input())
    while times:
        l, r = [int(x) for x in input().split(" ")]
        if l==r:
            print(0)
        else:
            answer = find_largest(l, r, (l + r)//2)
            print(answer)
        times -= 1
main()