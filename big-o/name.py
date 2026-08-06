import timeit

sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]

print(f"{'Size':>12} {'Time (μs)':>12}")
for n in sizes:
    lst = list(range(n))
    # time indexing near the middle, repeated many times
    t = timeit.timeit(lambda: lst[n // 2], number=10_000)
    print(f"{n:>12,} {t * 1e6 / 10_000:>12.4f}")
