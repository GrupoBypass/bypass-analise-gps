from memory_profiler import memory_usage
import algas
import time


def test_process(n, func):
    inicio = time.time()
    for i in range(1, n):
        func(algas.sum_of_n_init(i))
    fim = time.time()
    tempo_processamento = fim - inicio
    return tempo_processamento


def get_results(n, func):
    print("get_resuls start")
    memory_result = []
    time_result = []

    for iteration in range(0, n):
        mem_usage, process_time = memory_usage(
            (test_process, (n, func), {}), max_usage=True, retval=True
        )

        memory_result.append(mem_usage)
        time_result.append(process_time)

    print("get_resuls end")
    return memory_result, time_result
