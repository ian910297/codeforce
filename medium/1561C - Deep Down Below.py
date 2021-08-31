

def main():
    times = eval(input())
    while times:
        caves = eval(input())
        cave_info = []
        for i in range(caves):
            cave_info.append([int(x) for x in input().split(" ")])
            cave_info[i] = cave_info[i][1:]

        sorted_info = []
        # find maximal value by each cave
        # float('inf')
        # float('-inf')
        for i in range(caves):
            maxi_monster_value = cave_info[i][0]
            maxi_monster_idx = 0
            for j in range(1, len(cave_info[i])):
                if maxi_monster_value < cave_info[i][j]:
                    maxi_monster_value = cave_info[i][j]
                    maxi_monster_idx = j
        
            sorted_info.append((maxi_monster_value, maxi_monster_idx, i))

        from operator import itemgetter, attrgetter
        # sorted(student_tuples, key=itemgetter(2))
        # sorted(student_tuples, key=itemgetter(1,2))
        # sorted(student_tuples, key=itemgetter(2), reverse=True)
        # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
        # sorted(student_objects, key=attrgetter('age'))
        sorted_info = sorted(sorted_info, key=itemgetter(0), reverse=True)

        # backtrace
        answer = sorted_info[0][0] + 1
        cave_idx = sorted_info[0][2]
        monster_idx = sorted_info[0][1]
        for i in range(caves):
            if i != 0:
                cave_idx = sorted_info[i][2]
                monster_idx = len(cave_info[cave_idx]) - 1

            # start to walk
            while monster_idx >= 0:
                # print(i, cave_idx, monster_idx, answer)
                if answer < cave_info[cave_idx][monster_idx]:
                    answer = cave_info[cave_idx][monster_idx] + 1
                monster_idx -= 1
                answer -= 1
        print(answer + 1)
        times -= 1

main()