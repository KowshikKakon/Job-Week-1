import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")

with Timer():

    total = sum(i*i for i in range(1000000))