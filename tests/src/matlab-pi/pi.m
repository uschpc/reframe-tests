% Estimate pi using local parpool

cluster = parallel.cluster.Local;
nproc = str2num(getenv('SLURM_CPUS_PER_TASK')) - 1;
pool = parpool(cluster,nproc);

% Start timer
tic 

% Max number of points
max = 1e5;

% Number of points inside circle
n = 0;

parfor i = 1:max
    x=rand;
    y=rand;
    if(x^2 + y^2 < 1.0)
        n = n + 1;
    end
end

% Compute resulting value of pi
est = (4.0 * n / max);

% End timer
elapsed = toc;

% Display results
fprintf("pi = %f, elapsed time = %f\n", est, elapsed)

delete(pool)
