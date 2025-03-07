import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_CUDA_LU_L40S(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark for NVIDIA L40S"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:gpu",
        "endeavour:qcbgpu"
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
            "Mop/s_total": (700000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=l40s:1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification Successful", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
