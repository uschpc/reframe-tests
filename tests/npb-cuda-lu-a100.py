# NAS Parallel Benchmarks LU benchmark test
# Translated to CUDA
# For NVIDIA A100 GPU
# Purpose of test
# - Test CUDA module access
# - Test building CUDA program
# - Test running CUDA program
# - Test node and NVIDIA A100 GPU performance for flow solver
#   using Lower-Upper Symmetric-Gauss-Seidel method

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_CUDA_LU_A100(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark for NVIDIA A100"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-cuda-12.6.3"
    ]
    sourcesdir = "src/npb-cuda-lu"
    executable = "lu.D"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-cuda-lu.sh"
    ]
    reference = {
        "*": {
            "Mop/s_total": (544000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=a100:1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification Successful", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
