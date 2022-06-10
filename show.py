import matplotlib as plt


def ShowONe(filename):
    with open(filename) as f:
        for _ in xrange(1):
            next(f)
        nx = round((x_end - x_begin) / h) + 1
        nt = round((t_end - t_begin) / tau) + 1
        x = np.linspace(x_begin, x_end, nx)
        fig, ax = plt.subplots()
        ax.plot(x,, label='')
        ax.plot(x, 'r', label='')
        ax.legend()

        ax.set(xlabel='x', ylabel='y',
        ax.grid()

        plt.show()

