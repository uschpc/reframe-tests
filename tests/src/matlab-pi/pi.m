% Estimate pi using Monte Carlo method in parallel

tic;

cluster = parallel.cluster.Local;
nproc = str2double(getenv("SLURM_CPUS_PER_TASK"));
pool = parpool(cluster, nproc);

% Estimate pi using n points
n = 5000000000;

% Chunk number of points for parallel processing
% Limit chunk size to limit memory usage
chunk_size = 3000000;
quo = floor(n / chunk_size);
rem = mod(n, chunk_size);
chunks = repmat([chunk_size], 1, quo);
if rem ~= 0
    chunks(end + 1) = rem;
end

% Calculate number of points in the unit circle out of n points
counts = zeros(length(chunks), 1);
parfor i = 1:length(chunks)
    x = rand(chunks(i), 1);
    y = rand(chunks(i), 1);
    counts(i) = sum((x .* x) + (y .* y) <= 1);
end
total = sum(counts);

res = 4 * total / n;

delete(pool);

elapsed = toc;

fprintf("Estimate of pi: %f\n", res)
fprintf("Elapsed time: %f\n", elapsed)
