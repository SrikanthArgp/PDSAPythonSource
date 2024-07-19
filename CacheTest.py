from functools import cache, lru_cache
from timeit import repeat

@lru_cache(maxsize=2)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


# if __name__ == '__main__':
setup_code = "from __main__ import main"
stmt = "main()"
times = repeat(setup=setup_code, stmt=stmt, repeat=2, number=4)
print(f"Minimum execution time: {min(times)}")
# main()