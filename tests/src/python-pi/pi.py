# Estimate pi using Monte Carlo method in parallel

import concurrent.futures
import os
import random
import time

# Calculate number of points in the unit circle out of n points
def monte_carlo_points(n):
    rand = random.random
    count = 0
    for _ in range(n):
        x = rand()
        y = rand()
        if (x * x) + (y * y) <= 1.0:
            count += 1
    return count

# Estimate pi using n points
def est_pi(n):
    # Chunk number of points for parallel processing
    # Set number of chunks to number of cores
    nchunks = int(os.environ["SLURM_CPUS_PER_TASK"])
    quo, rem = divmod(n, nchunks)
    chunks = [quo] * nchunks
    chunks[0] += rem
    with concurrent.futures.ProcessPoolExecutor(nchunks) as executor:
        total = sum(executor.map(monte_carlo_points, chunks))
    return 4.0 * total / n

if __name__ == "__main__":
    start = time.perf_counter()

    res = est_pi(5000000000)

    end = time.perf_counter()
    elapsed = end - start

    print("Estimate of pi:", res)
    print("Elapsed time:", elapsed)
