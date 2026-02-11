# NAS Parallel Benchmarks OpenMP MG (multigrid) benchmark test
# Translated to C++
# Purpose of test
# - Test compiler module access
# - Test building C++/OpenMP program
# - Test running C++/OpenMP program
# - Test node performance for differential equations solver
#   using multigrid method
# Notes
# - https://github.com/GMAP/NPB-CPP
# - Requires a power-of-two number of CPU cores

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_cpp_omp_mg(rfm.RunOnlyRegressionTest):
    descr = "NPB CPP OpenMP MG benchmark"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:epyc-7513",
        "endeavour:epyc-7513",
        "pathfinder:xeon-2640v3",
        "laguna:epyc-9554"
    ]
    valid_prog_environs = [
        "env-gcc-14.3.0",
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/npb-cpp-omp"
    executable = "$TMPDIR/NPB-CPP/NPB-OMP/bin/mg.D"
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_ON_NODE"
    }
    prerun_cmds = [
        "bash make-npb-cpp-omp.sh mg D"
    ]
    reference = {
        "discovery:epyc-7513": {
            "Mop/s_total": (63000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7513": {
            "Mop/s_total": (63000, -0.1, 0.1, "Mop/s")
        },
        "pathfinder:xeon-2640v3": {
            "Mop/s_total": (22000, -0.1, 0.1, "Mop/s")
        },
        "laguna:epyc-9554": {
            "Mop/s_total": (166000, -0.1, 0.1, "Mop/s")
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
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
