# NAS Parallel Benchmarks OpenMP EP (embarrassingly parallel) benchmark test
# Purpose of test
# - Test compiler module access
# - Test building Fortran/OpenMP program
# - Test running Fortran/OpenMP program
# - Test node performance targeting maximum flop/s
# Notes
# - Requires a power-of-two number of CPU cores

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_OMP_EP(rfm.RunOnlyRegressionTest):
    descr = "NPB OpenMP EP benchmark"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:epyc-9534",
        "discovery:epyc-9354",
        "discovery:epyc-7513",
        "discovery:epyc-7313",
        "discovery:epyc-7542",
        "discovery:epyc-7282",
        "discovery:xeon-6130",
        "discovery:xeon-4116",
        "discovery:xeon-2640v4",
        "endeavour:allnodes",
        "pathfinder:allnodes",
        "laguna:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/npb-omp"
    executable = "ep.D.x"
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_ON_NODE"
    }
    prerun_cmds = [
        "bash make-npb-omp.sh ep D"
    ]
    reference = {
        "discovery:epyc-9534": {
            "Mop/s_total": (4084, -0.1, None, "Mop/s")
        },
        "discovery:epyc-9354": {
            "Mop/s_total": (4084, -0.1, None, "Mop/s")
        },
        "discovery:epyc-7513": {
            "Mop/s_total": (4084, -0.1, None, "Mop/s")
        },
        "discovery:epyc-7313": {
            "Mop/s_total": (2074, -0.1, None, "Mop/s")
        },
        "discovery:epyc-7542": {
            "Mop/s_total": (1500, -0.1, None, "Mop/s")
        },
        "discovery:epyc-7282": {
            "Mop/s_total": (1500, -0.1, None, "Mop/s")
        },
        "discovery:xeon-6130": {
            "Mop/s_total": (1174, -0.1, None, "Mop/s")
        },
        "discovery:xeon-4116": {
            "Mop/s_total": (1174, -0.1, None, "Mop/s")
        },
        "discovery:xeon-2640v4": {
            "Mop/s_total": (1092, -0.1, None, "Mop/s")
        },
        "*": {
            "Mop/s_total": (900, -0.1, None, "Mop/s")
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
