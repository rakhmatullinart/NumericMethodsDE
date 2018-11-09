from PyQt5.QtWidgets import QTabWidget

from SolvingMethods import Grid
from tabs import Tab


class TabWindow(QTabWidget):
    def __init__(self):
        super(TabWindow, self).__init__()
        self.tabs_names = ['Methods', 'Local errors', 'Approximation Errors']
        self.tabs = {str: Tab}
        self.tabs = {k: v for k, v in zip(self.tabs_names, (Tab(self) for i in range(len(self.tabs_names))))}

        self.insert_tabs()

    def insert_tabs(self):
        for name, tab in self.tabs.items():
            self.addTab(tab, name)

    def plot_on_tabs(self, tab_no: int, methods: {str: Grid}, terminal_n=100):
        tab = self.tabs.get(self.tabs_names[tab_no])
        tab.figure.clear()
        ax = tab.figure.add_subplot(111)

        colors = ['r', 'g', 'b', 'yellow']
        m_colors = dict(zip(methods.keys(), colors))

        if tab_no == 0:
            for key, v in methods.items():
                v.solve()
                ax.plot(v.x, v.y, m_colors.get(key), label=key)
            ax.set_title("Numeric Methods")
            ax.set_xlabel('X')
            ax.set_ylabel('Y')

        elif tab_no == 1:
            data_local_errors = {k: [v.x, v.get_local_error(methods.get('Exact').y)] for k, v in methods.items()}
            data_local_errors.pop('Exact')

            for key, v in data_local_errors.items():
                ax.plot(v[0], v[1], m_colors.get(key), label=key)
            ax.set_title("Local errors")
            ax.set_xlabel('X')
            ax.set_ylabel('Error')

        elif tab_no == 2:
            terminal_n = 100 if terminal_n < 30 else terminal_n

            for key, v in methods.items():
                if key == 'Exact':
                    continue
                x, er = v.get_approximation_error(terminal_n)
                ax.plot(x, er, m_colors.get(key), label=key)
            ax.set_title("Total approximation errors")
            ax.set_xlabel('N')
            ax.set_ylabel('Total approximation error')

        ax.grid()
        ax.legend(loc='upper right')
        tab.canvas.draw()
        tab.toolbar.update()
