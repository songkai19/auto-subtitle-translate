from typing import Iterator
import time

from .translate_worker import line_tt

result_list = []


def run(transcript: Iterator[dict]):
    print(f"Start translating the subtitles.")

    start = time.time()

    for subtitle in transcript:
        result_list.append(line_tt(subtitle))

    print(f"Time taken = {time.time() - start:.10f}")

    print(result_list)
    return result_list