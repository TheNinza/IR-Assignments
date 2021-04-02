"""
Fabrik IR

By: Nikhil Gupta (2019BCS-036)

"""

import matplotlib.pyplot as plt


def eucledian_distance(p1, p2):

    return (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**0.5


def fabrik_solver(p, goal, tolerence):

    b = p[0]
    diff = eucledian_distance(p[-1], goal)

    number_iterations = 0

    while diff > tolerence:
        # forward reaching
        p[-1] = goal
        for i in range(len(p)-2, -1, -1):
            r = eucledian_distance(p[i+1], p[i])
            lam = l[i]/r
            p[i] = ((1-lam)*p[i+1][0] + lam*p[i][0],
                    (1-lam)*p[i+1][1] + lam*p[i][1])

        # backward reaching
        p[0] = b
        for i in range(len(p)-1):
            r = eucledian_distance(p[i+1], p[i])
            lam = l[i]/r
            p[i+1] = ((1-lam)*p[i][0] + lam*p[i+1][0],
                      (1-lam)*p[i][1] + lam*p[i+1][1])

        diff = eucledian_distance(p[-1], goal)

        number_iterations += 1

    return p, number_iterations


def print_solution(p, number_iterations):

    print('\nNumber of iterations = {}'.format(number_iterations))

    print('New Joint positions are:')
    for i in range(len(p)):
        print(p[i])


def plot_graph(p, new_p, goal):

    p_x = []
    p_y = []
    for coord in p:
        p_x.append(coord[0])
        p_y.append(coord[1])

    new_p_x = []
    new_p_y = []
    for coord in new_p:
        new_p_x.append(coord[0])
        new_p_y.append(coord[1])

    plt.plot(p_x, p_y, label='Original Positions', marker='o')
    plt.plot(new_p_x, new_p_y, label='New Positions', marker='o')
    plt.scatter([goal[0]], [goal[1]], s=400, marker='*', label='Goal')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Taking input
    p = []
    for i in range(4):
        temp = tuple(
            map(float, input('Enter initial position of joint {}: '.format(i)).split()))
        p.append(temp)

    goal = tuple(
        map(float, input('Enter goal position of end effector: ').split()))

    tolerence = float(input('Enter tolerance: '))

    dist = eucledian_distance(p[0], goal)

    l = []
    for i in range(len(p)-1):
        l.append(eucledian_distance(p[i], p[i+1]))

    # Checking if the goal state is reachable
    if dist > sum(l):
        print('Goal unreachable')
        exit()

    new_p, number_iterations = fabrik_solver(p.copy(), goal, tolerence)

    print_solution(new_p, number_iterations)

    plot_graph(p, new_p, goal)