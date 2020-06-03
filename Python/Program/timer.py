import time

class Timer(object):
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args):
        self._end = time.time()
        self.secs = self._end - self._start
        print("[INFO] time cost %.2fs" % self.secs)


if __name__ == "__main__":
    with Timer() as t:
        for i in range(999):
            print(i)
