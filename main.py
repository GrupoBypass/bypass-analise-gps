from modules import test as t, plot as plt, save as s

from modules.sensor import gps

if __name__ == "__main__":

    n = 100
    res = t.get_results(
        n, lambda: gps.calc_distance())
    )

    print(res)

    plt.plot_results(n, res[0], res[1])
    s.save_results(n, res[0], res[1])
