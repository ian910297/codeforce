

def main():
    times = eval(input())
    while times:
        caves = eval(input())
        cave_info = []
        for i in range(caves):
            cave_info.append([int(x) for x in input().split(" ")])
            cave_info[i] = cave_info[i][1:]

        sorted_info = []
        # # find maximal value by each cave
        # # float('inf')
        # # float('-inf')
        for i in range(caves):
            tmp_answer = cave_info[i][0] + 1
            tmp_power = tmp_answer
            for j in range(1, len(cave_info[i])):
                tmp_power += 1
                if tmp_power < cave_info[i][j]:
                    tmp_answer = cave_info[i][j] + 1 - j
                    tmp_power = cave_info[i][j] + 1
        
            sorted_info.append((tmp_answer, i))

        from operator import itemgetter, attrgetter
        # # sorted(student_tuples, key=itemgetter(2))
        # # sorted(student_tuples, key=itemgetter(1,2))
        # # sorted(student_tuples, key=itemgetter(2), reverse=True)
        # # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
        # # sorted(student_objects, key=attrgetter('age'))
        sorted_info = sorted(sorted_info, key=itemgetter(0))

        for i in range(caves):
            if i == 0:
                answer = sorted_info[0][0]
                power = sorted_info[0][0]
                steps = len(cave_info[sorted_info[0][1]])
            else:
                steps += len(cave_info[sorted_info[i - 1][1]])
                if power + len(cave_info[sorted_info[i - 1][1]]) < sorted_info[i][0]:
                    diff = sorted_info[i][0] - (power + len(cave_info[sorted_info[i - 1][1]]))
                    answer += diff
                    power = sorted_info[i][0]
                else:
                    power += steps

        print(answer)
        times -= 1

main()