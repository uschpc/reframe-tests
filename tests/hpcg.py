import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class HPCG(rfm.RunOnlyRegressionTest):
    descr = "HPCG benchmark using 10 epyc-7513 nodes"
    valid_systems = [
        "discovery:epyc-64",
        "discovery:main",
        "endeavour:priya"
    ]
    valid_prog_environs = [
        "PrgEnv-hpcg"
    ]
    sourcesdir = None
    executable = "xhpcg"
    executable_opts = ["--nx=128", "--ny=128", "--nz=128", "--rt=120"]
    num_tasks = 640
    num_tasks_per_node = 64
    num_cpus_per_task = 1
    time_limit = "10m"
    output_file = sn.getitem(sn.glob("HPCG-Benchmark*.txt"), 0)
    prerun_cmds = [
        "ulimit -s unlimited"
    ]
    env_vars = {
        "OMP_NUM_THREADS": "1",
        "SLURM_MPI_TYPE": "pmix_v2",
        "SLURM_CPU_BIND": "verbose"
    }
    reference = {
        "*": {
            "gflops": (330, -0.1, None, "gflops")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--constraint=epyc-7513",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"HPCG result is VALID", self.output_file)

    @performance_function("gflops", perf_key = "gflops")
    def extract_perf(self):
        return sn.extractsingle(r"GFLOP/s rating of=(?P<gflops_ret>[0-9]+.[0-9]+)", self.output_file, "gflops_ret", float)
