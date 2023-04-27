from sys import stdin, exit


land_col_size, land_row_size = map(int, stdin.readline().split())

num_of_robots, num_of_commands = map(int, stdin.readline().split())

robots = []
commands = []

check = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(num_of_robots):
    robot_x, robot_y, face = stdin.readline().split()

    if face == 'N':
        direction = 0

    elif face == 'E':
        direction = 1

    elif face == 'S':
        direction = 2

    elif face == 'W':
        direction = 3

    robots.append([int(robot_x), int(robot_y), direction])

for _ in range(num_of_commands):
    robot_no, command, repeat = stdin.readline().split()
    commands.append([int(robot_no), command, int(repeat)])

for robot_no, command, repeat in commands:
    for _ in range(repeat):

        if command == 'F':
            robots[robot_no - 1][0] += check[robots[robot_no - 1][2]][1]
            robots[robot_no - 1][1] += check[robots[robot_no - 1][2]][0]

            if robots[robot_no - 1][0] > land_col_size or robots[robot_no - 1][0] <= 0 or robots[robot_no - 1][1] > land_row_size or robots[robot_no - 1][1] <= 0:
                print(f'Robot {robot_no} crashes into the wall')
                exit(0)

            for other in range(num_of_robots):
                if other != robot_no - 1:
                    if robots[robot_no - 1][0] == robots[other][0] and robots[robot_no - 1][1] == robots[other][1]:
                        print(f'Robot {robot_no} crashes into robot {other + 1}')
                        exit(0)

        elif command == 'L':
            robots[robot_no - 1][2] = (robots[robot_no - 1][2] - 1) % 4

        elif command == 'R':
            robots[robot_no - 1][2] = (robots[robot_no - 1][2] + 1) % 4

print('OK')
