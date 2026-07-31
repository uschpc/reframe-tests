# NAS Parallel Benchmarks LU benchmark test
# Translated to CUDA
# Purpose of test
# - Test CUDA 13 module access
# - Test building CUDA program
# - Test running CUDA program
# - Test GPU performance for flow solver
#   using Lower-Upper Symmetric-Gauss-Seidel method
# Notes
# - https://github.com/GMAP/NPB-GPU
# - Assumes all GPUs on node are the same model

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_cuda_lu(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark"
    tags = {
        "gpu",
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:l40s",
        "discovery:a100",
        "discovery:a40",
        "endeavour:h200",
        "endeavour:l40s",
        "endeavour:a100",
        "endeavour:a40",
        "laguna:l40s"
    ]
    valid_prog_environs = [
        "gcc-15.3.0-cuda-13.0.3"
    ]
    sourcesdir = "src/npb-cuda"
    executable = "sleep 1s"
    time_limit = "5m"
    prerun_cmds = [
        "echo SLURM_GPUS_ON_NODE=$SLURM_GPUS_ON_NODE",
        "bash run-npb-cuda-lu.sh"
    ]
    reference = {
        "discovery:l40s": {
            "Mop/s_total": (414000, -0.05, 0.05, "Mop/s")
        },
        "discovery:a100": {
            "Mop/s_total": (560000, -0.1, 0.1, "Mop/s")
        },
        "discovery:a40": {
            "Mop/s_total": (161000, -0.05, 0.05, "Mop/s")
        },
        "endeavour:h200": {
            "Mop/s_total": (1265000, -0.05, 0.05, "Mop/s")
        },
        "endeavour:l40s": {
            "Mop/s_total": (414000, -0.05, 0.05, "Mop/s")
        },
        "endeavour:a100": {
            "Mop/s_total": (588000, -0.05, 0.05, "Mop/s")
        },
        "endeavour:a40": {
            "Mop/s_total": (161000, -0.05, 0.05, "Mop/s")
        },
        "laguna:l40s": {
            "Mop/s_total": (414000, -0.05, 0.05, "Mop/s")
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
