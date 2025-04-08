# NAS Parallel Benchmarks OpenMP MG (multigrid) benchmark test
# Purpose of test
# - Test compiler module access
# - Test building Fortran/OpenMP program
# - Test running Fortran/OpenMP program
# - Test node performance for differential equations solver
#   using multigrid method
# Notes
# - Requires a power-of-two number of CPU cores

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_OMP_MG(rfm.RunOnlyRegressionTest):
    descr = "NPB OpenMP MG benchmark"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/npb-omp-mg"
    executable = "mg.D.x"
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_ON_NODE"
    }
    prerun_cmds = [
        "bash make-npb-omp-mg.sh"
    ]
    reference = {
        "*": {
            "Mop/s_total": (26000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--exclusive",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"VERIFICATION SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
