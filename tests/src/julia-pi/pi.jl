# Estimate pi in parallel using multiple threads

using Base.Threads
using Random

# Calculate the number of points in the unit circle out of n points
function monte_carlo_pi_part(n)
    rng = Xoshiro()
    # If within the unit circle
    return sum(rand(rng)^2 + rand(rng)^2 < 1 for i = 1:n)
end

# Estimate pi using n points
function est_pi(n)
    # One task per thread
    # One chunk of points per task
    nchunks = nthreads()
    chunk = ceil(Int, n / nchunks)
    tasks = map(1:nchunks) do task
        @spawn monte_carlo_pi_part(chunk)
    end
    total = mapreduce(fetch, +, tasks)
    return 4 * (total / n)
end

res = @timed est_pi(5000000000)

println("Estimate of pi: ", res.value)
println("Elapsed time: ", res.time)
