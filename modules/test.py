from memory_profiler import memory_usage
import time


def test_process(func):
    inicio = time.time()
    func()
    fim = time.time()
    tempo_processamento = fim - inicio
    return tempo_processamento


def get_results(n, func):
    print ("get_resuls start")
    memory_result = []
    time_result = []

    for iteration in range(0,n):
        mem_usage, process_time = memory_usage(
            (test_process, (func,), {}), max_usage=True, retval=True
        )

        memory_result.append(mem_usage)
        time_result.append(process_time)

    print ("get_resuls end")
    return memory_result, time_result
