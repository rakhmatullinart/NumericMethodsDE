import numpy as np

class Grid:

    def __init__(self, x0, y0, xn, n):
        n = int(n)

        self.step = (xn - x0) / n
        self.no_of_steps = n

        self.x = np.arange(x0, xn, self.step)
        self.__calculate_const(x0, y0)

        self.y = np.zeros(len(self.x))
        self.y[0] = y0

    @staticmethod
    def f(x, y):
        return 4/x/x - y/x - y*y

    def __calculate_const(self, x0, y0):
        self.__const = (x0 * y0 + 2)/(x0**5 * y0 - 2 * x0**4)

    def exact_solution(self, x):
        return 4/(-x + self.__const * (x ** 5)) + 2/x

    def solve(self):
        pass

    def get_local_error(self, exact_y):
        local_errors = abs(self.y - exact_y)
        return local_errors

    def get_approximation_error(self, terminal_n):
        x0 = self.x[0]
        y0 = self.y[0]
        xn = self.x[-1]
        x = [i for i in range(20, terminal_n + 1)]
        global_error = [0 for i in range(20, terminal_n + 1, 1)]

        for i in range(len(x)):
            exact = Exact(x0, y0, xn, x[i])
            exact.solve()
            exact_y = exact.y
            self.__init__(x0, y0, xn, x[i])
            self.solve()
            approx_y = self.y

            e = max(abs(approx_y - exact_y))
            global_error[i] = e

        return x, global_error


class Exact(Grid):
    def solve(self):
        for i in range(len(self.y)):
            self.y[i] = self.exact_solution(self.x[i])


class Euler(Grid):

    def solve(self):
        for i in range(len(self.x) - 1):
                self.y[i + 1] = self.y[i] + self.step * self.f(self.x[i], self.y[i])


class ImprovedEuler(Grid):

    def solve(self):
        for i in range(len(self.x) - 1):  # indexing each point in corresponding part
            k1 = self.f(self.x[i], self.y[i])
            k2 = self.f(self.x[i] + self.step, self.y[i] + self.step * k1)  # writing to the next

            self.y[i + 1] = self.y[i] + self.step * (k1 + k2)/2


class RungeKutta(Grid):

    def solve(self):
        for i in range(len(self.x) - 1):
            x_ith, y_ith = self.x[i], self.y[i]
            k1 = self.f(x_ith, self.y[i])
            k2 = self.f(x_ith + self.step / 2, y_ith + self.step * k1 / 2)
            k3 = self.f(x_ith + self.step / 2, y_ith + self.step * k2 / 2)
            k4 = self.f(x_ith + self.step, y_ith + self.step * k3)

            self.y[i + 1] = y_ith + self.step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
