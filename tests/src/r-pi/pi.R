# Estimate pi using Monte Carlo method in parallel

library(parallel)

# Calculate number of points in the unit circle out of n points
monte_carlo_points <- function(n) {
    x <- runif(n)
    y <- runif(n)
    return(sum((x * x) + (y * y) <= 1))
}

# Estimate pi using n points
est_pi <- function(n) {
    # Chunk number of points for parallel processing
    # Limit chunk size to limit memory usage
    chunk_size <- 3000000
    quo <- n %/% chunk_size
    rem <- n %% chunk_size
    chunks <- rep(chunk_size, quo)
    if (rem != 0) chunks <- c(chunks, rem)
    cores <- as.integer(Sys.getenv("SLURM_CPUS_PER_TASK"))
    tasks <- mclapply(chunks, monte_carlo_points, mc.cores = cores)
    total <- sum(unlist(tasks))
    return(4 * total / n)
}

start <- Sys.time()

res <- est_pi(5000000000)

end <- Sys.time()
elapsed <- difftime(end, start, units = "secs")

cat("Estimate of pi:", res, "\n")
cat("Elapsed time:", elapsed, "\n")
