from typing import Iterator
import multiprocessing
import time

from .translate_worker import line_tt

PROCESSES = multiprocessing.cpu_count() - 1
result_list = []


def delay_exe(seconds):
    time.sleep(seconds)

def run(transcript: Iterator[dict]):
    print(f"Running with {PROCESSES} processes!")

    start = time.time()

    # mutli-processing implementation -> failed due to the request limit
    with multiprocessing.Pool(PROCESSES) as p:
        result = p.map_async(
            line_tt,
            transcript,
            chunksize=10,
            callback=delay_exe(60)
        )

        # clean up
        p.close()
        p.join()

    for value in result.get():
        # todo
        result_list.append(value)
        
    print(f"Time taken = {time.time() - start:.10f}")

    # print(result_list)
    return result_list

