# NAS Parallel Benchmarks LU benchmark test
# Translated to CUDA
# For NVIDIA RTX5000 GPU
# Purpose of test
# - Test CUDA module access
# - Test building CUDA program
# - Test running CUDA program
# - Test node and NVIDIA RTX5000 GPU performance for flow solver
#   using Lower-Upper Symmetric-Gauss-Seidel method

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_CUDA_LU_RTX5000(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark for NVIDIA RTX5000"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-cuda-12.6.3"
    ]
    sourcesdir = "src/npb-cuda"
    executable = "lu.C"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-cuda.sh lu C"
    ]
    reference = {
        "*": {
            "Mop/s_total": (75000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=rtx5000:1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
