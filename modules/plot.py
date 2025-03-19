import matplotlib.pyplot as plt


def plot_results(n, memory_result, time_result):
    fig, ax1 = plt.subplots()

    color = "tab:red"
    ax1.set_xlabel("Valor Somado")
    ax1.set_ylabel("Memória Usada (MiB)", color=color)
    ax1.plot(n, memory_result, "o-", color=color, label="Memoria Usada")
    ax1.tick_params(axis="y", labelcolor=color)

    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("Tempo de execução (segundos)", color=color)
    ax2.plot(n, time_result, "s-", color=color, label="Tempo de execução")
    ax2.tick_params(axis="y", labelcolor=color)

    fig.tight_layout()
    plt.title("Memória Usada e Tempo de execução vs Valor Somado")
    plt.show()
