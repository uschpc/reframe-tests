# Estimate pi using Monte Carlo method in parallel

using Base.Threads
using Random

# Calculate number of points in the unit circle out of n points
function monte_carlo_points(n)
    count = 0
    for _ in 1:n
        x = rand()
        y = rand()
        if (x * x) + (y * y) <= 1.0
            count += 1
        end
    end
    return count
end

# Estimate pi using n points
function est_pi(n)
    # Chunk number of points for parallel processing
    # Set number of chunks to number of threads
    nchunks = nthreads()
    quo, rem = divrem(n, nchunks)
    chunks = fill(quo, nchunks)
    chunks[1] += rem
    tasks = [@spawn monte_carlo_points(chunk) for chunk in chunks]
    total = sum(fetch, tasks)
    return 4.0 * total / n
end

res = @timed est_pi(5000000000)

println("Estimate of pi: ", res.value)
println("Elapsed time: ", res.time)
