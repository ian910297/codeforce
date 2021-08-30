import math
prime_set = []

def is_prime(target):
    if target == 1:
        return False
    if target == 2:
        prime_set.append(target)
        return True

    if target in prime_set:
        return True

    # check it is even or odd
    if (target & 1) == 0:
        return False

    end = int(math.sqrt(target))
    i = 3
    while i <= end:
        if (target % i) == 0:
            return False
        i += 2

    prime_set.append(target)
    return True

def permutations(target):
    import itertools
    pre_set = list(target)
    for i in range(1, len(pre_set)+1):
        # order matters
        # print(list(itertools.permutations(pre_set, i)))
        # order does not matter
        tmp = list(itertools.combinations(pre_set, i))
        for j in range(len(tmp)):
            if '0' in tmp[j]:
                continue
            t = int("".join(tmp[j]))
            # print(t, tmp[j])
            ret = is_prime(t)
            if ret == False:
                return True, t, i
    
    return False, None, None


def main():
    times = eval(input())
    while times:
        nothing = input()
        target = input()
        ret, value, length = permutations(target)
        print(length)
        print(value)
        times -= 1
main()