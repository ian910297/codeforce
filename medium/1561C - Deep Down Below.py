

def main():
    times = eval(input())
    while times:
        caves = eval(input())
        cave_info = []
        for i in range(caves):
            cave_info.append([int(x) for x in input().split(" ")])
            cave_info[i] = cave_info[i][1:]

        # sorted_info = []
        # # find maximal value by each cave
        # # float('inf')
        # # float('-inf')
        # for i in range(caves):
        #     maxi_monster_value = cave_info[i][0]
        #     maxi_monster_idx = 0
        #     for j in range(1, len(cave_info[i])):
        #         if maxi_monster_value < cave_info[i][j]:
        #             maxi_monster_value = cave_info[i][j]
        #             maxi_monster_idx = j
        
        #     sorted_info.append((maxi_monster_value, maxi_monster_idx, i))

        # from operator import itemgetter, attrgetter
        # # sorted(student_tuples, key=itemgetter(2))
        # # sorted(student_tuples, key=itemgetter(1,2))
        # # sorted(student_tuples, key=itemgetter(2), reverse=True)
        # # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
        # # sorted(student_objects, key=attrgetter('age'))
        # sorted_info = sorted(sorted_info, key=itemgetter(0), reverse=True)

        visited_cave = []
        answer = None
        power = None
        while len(visited_cave) < caves:
            candidate_idx = None
            candidate_answer = None
            candidate_power = None
            for cave_idx in range(caves):
                if cave_idx in visited_cave:
                    continue
                
                # first round
                if answer == None:
                    current_answer = None
                    current_power = None
                else:
                    current_answer = answer
                    current_power = power

                # walk
                for monster_idx in range(0, len(cave_info[cave_idx])):
                    if current_answer == None:
                        current_answer = cave_info[cave_idx][monster_idx] + 1
                        current_power = current_answer + 1
                        continue

                    if current_power <= cave_info[cave_idx][monster_idx]:
                        # print("current_answer({}) = current_power({}) - current_steps({})".format(current_answer, current_power, current_steps))
                        current_answer -= current_power
                        current_power = cave_info[cave_idx][monster_idx] + 1
                        current_answer += current_power

                    current_power += 1

                # store info
                if candidate_idx == None or candidate_answer > current_answer:
                    # print("store", cave_idx, current_answer, current_power)
                    candidate_idx = cave_idx
                    candidate_answer = current_answer
                    candidate_power = current_power
            visited_cave.append(candidate_idx)
            # print("answer", candidate_answer, current_steps)
            answer = candidate_answer
            power = candidate_power

        print(answer)
        times -= 1

main()