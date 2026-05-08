from logab import log_wrap, log_init
from fire import Fire
import time
from dataclasses import dataclass, asdict

@dataclass
class CustomClass:
    def fast(self):
        logger = log_init()
        start_time=time.perf_counter()
        for i in range(100):
            # logger.info(i)
            print(i)
        end_time=time.perf_counter()
        print(f"Time take: {end_time-start_time}")
    def slow(self):
        for i in range(100):
            time.sleep(0.5)
            start_time=time.perf_counter()
            print(i)
            end_time=time.perf_counter()
            print(f"Time take: {end_time-start_time}")

if __name__=="__main__":
    with log_wrap():
        Fire(CustomClass)