# NAS Parallel Benchmarks LU benchmark test
# Translated to CUDA
# Purpose of test
# - Test CUDA module access
# - Test building CUDA program
# - Test running CUDA program
# - Test GPU performance for flow solver
#   using Lower-Upper Symmetric-Gauss-Seidel method

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_cuda_lu(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:l40s",
        "discovery:a100",
        "discovery:a40",
        "discovery:v100",
        "discovery:p100",
        "endeavour:l40s",
        "endeavour:a100",
        "endeavour:a40",
        "endeavour:v100",
        "endeavour:p100",
        "endeavour:rtx5000",
        "laguna:l40s"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-cuda-12.6.3"
    ]
    sourcesdir = "src/npb-cuda"
    executable = "sleep 1s"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "echo SLURM_GPUS_ON_NODE=$SLURM_GPUS_ON_NODE",
        "bash run-npb-cuda-lu.sh"
    ]
    reference = {
        "discovery:l40s": {
            "Mop/s_total": (414000, -0.1, None, "Mop/s")
        },
        "discovery:a100": {
            "Mop/s_total": (544000, -0.1, None, "Mop/s")
        },
        "discovery:a40": {
            "Mop/s_total": (161000, -0.1, None, "Mop/s")
        },
        "discovery:v100": {
            "Mop/s_total": (179000, -0.1, None, "Mop/s")
        },
        "discovery:p100": {
            "Mop/s_total": (133000, -0.1, None, "Mop/s")
        },
        "endeavour:l40s": {
            "Mop/s_total": (414000, -0.1, None, "Mop/s")
        },
        "endeavour:a100": {
            "Mop/s_total": (544000, -0.1, None, "Mop/s")
        },
        "endeavour:a40": {
            "Mop/s_total": (161000, -0.1, None, "Mop/s")
        },
        "endeavour:v100": {
            "Mop/s_total": (179000, -0.1, None, "Mop/s")
        },
        "endeavour:p100": {
            "Mop/s_total": (133000, -0.1, None, "Mop/s")
        },
        "endeavour:rtx5000": {
            "Mop/s_total": (75000, -0.1, None, "Mop/s")
        },
        "laguna:l40s": {
            "Mop/s_total": (414000, -0.1, None, "Mop/s")
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
        ngpus = sn.extractsingle(r"SLURM_GPUS_ON_NODE=(?P<ngpus>\S+)", self.stdout, "ngpus", int)
        matches = sn.findall(r"Verification\s+=\s+SUCCESSFUL", self.stdout)
        nmatches = sn.len(matches)
        return sn.assert_eq(nmatches, ngpus)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        res = sn.extractall(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
        return sn.avg(res)
