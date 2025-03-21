from modules import test as t, process as p, plot as plt, save as s

from modules.sensor import gps

if __name__ == "__main__":

    n = 100
    res = t.get_results(
        n, lambda: p.process_data(gps.get_position(), gps.get_position())
    )

    print(res)

    plt.plot_results(n, res[0], res[1])
    s.save_results(n, res[0], res[1])
