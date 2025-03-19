from modules import test as t, process as p, plot as plt, save as s

if __name__ == "__main__":
    n = 10
    res = t.get_results(n, p.process_data(p.get_position(), p.get_position()))

    print(res)

    plt.plot_results(n, res[0], res[1])
    s.save_results(n, res[0], res[1])
