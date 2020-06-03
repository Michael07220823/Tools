import time

class Timer(object):
    def __init__(self, string):
        self._string = string

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args):
        self.secends = time.time() - self._start
        print("[INFO] %s cost time %.4f secs." % (self._string, self.secends))


if __name__ == "__main__":
    with Timer("Test") as t:
        for i in range(999):
            print(i)
