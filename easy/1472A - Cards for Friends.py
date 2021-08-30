def main():
    times = eval(input())
    while times:
        raw_text = input()
        w, h, n = [int(x) for x in raw_text.split(' ')]
        pieces = 1
        while 1:
            if (w & 1) == 0:
                w >>= 1
            elif (h & 1) == 0:
                h >>= 1
            else:
                break
            pieces *= 2
        if pieces >= n:
            print("YES")
        else:
            print("NO")
        times -= 1

main()