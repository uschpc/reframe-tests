import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_CUDA_LU_A40(rfm.RunOnlyRegressionTest):
    descr = "NPB CUDA LU benchmark for NVIDIA A40"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:gpu",
        "discovery:debug",
        "endeavour:cryoem",
        "endeavour:isi",
        "endeavour:warshel"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-cuda-12.6.3"
    ]
    sourcesdir = "src/npb-cuda-lu"
    executable = "NPB-GPU/CUDA/bin/lu.D"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-cuda-lu.sh"
    ]
    reference = {
        "*": {
            "Mop/s_total": (200000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=a40:1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification Successful", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
