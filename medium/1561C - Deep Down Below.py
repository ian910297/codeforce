

def main():
    times = eval(input())
    while times:
        caves = eval(input())
        cave_info = []
        for i in range(caves):
            cave_info.append([int(x) for x in input().split(" ")])
            cave_info[i] = cave_info[i][1:]
        # print(cave_info)
        end_cave = 0
        end_cave_set = []
        steps = 0
        answer = None
        current_value = None
        while end_cave < caves:
            # find minimal head value
            # float('inf')
            # float('-inf')
            mini_cave_idx = None
            mini_cave_value = None
            for i in range(caves):
                # already visited
                if i in end_cave_set:
                    continue

                # first valid number
                if mini_cave_idx == None:
                    mini_cave_idx = i
                    mini_cave_value = cave_info[i][0]
                    continue

                # normal case
                if mini_cave_value > cave_info[i][0]:
                    mini_cave_idx = i
                    mini_cave_value = cave_info[i][0]
            # end
            if mini_cave_idx == None:
                break
            # record visited cave
            end_cave_set.append(mini_cave_idx)

            # start to walk
            for i in range(len(cave_info[mini_cave_idx])):
                if answer == None:
                    answer = cave_info[mini_cave_idx][i] + 1
                    current_value = answer + 1
                    continue
                
                if current_value < cave_info[mini_cave_idx][i]:
                    answer = cave_info[mini_cave_idx][i] + 1
                    current_value = answer + 1
                else:
                    current_value += 1
            
            end_cave += 1
        print(answer)
        times -= 1

main()