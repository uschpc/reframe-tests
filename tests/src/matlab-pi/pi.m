% Estimate pi using local parpool

cluster = parallel.cluster.Local;
nproc = str2num(getenv('SLURM_CPUS_PER_TASK'));
pool = parpool(cluster,nproc);

tic;

% Number of points to use for the pi estimation
n = 5000000000;

% Calculate the number of points in the unit circle out of n points
c = 0;
parfor i = 1:n
    x = rand;
    y = rand;
    if(x^2 + y^2 < 1.0)
        c = c + 1;
    end
end

% Estimate pi
est = 4.0 * (c / n);

delete(pool)

elapsed = toc;

% Display results
fprintf("Estimate of pi: %f\n", est)
fprintf("Elapsed time: %f\n", elapsed)
