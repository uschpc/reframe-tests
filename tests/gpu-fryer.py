# gpu-fryer test
# Purpose of test
# - Test Apptainer module access
# - Test Apptainer exec
# - Test Apptainer GPU access
# - Stress test all GPUs on node
# Notes
# - https://github.com/huggingface/gpu-fryer

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class gpu_fryer(rfm.RunOnlyRegressionTest):
    descr = "GPU stress test with gpu-fryer"
    tags = {
        "gpu",
        "singlenode",
        "stress"
    }
    valid_systems = [
        "discovery:l40s",
        "discovery:a100",
        "discovery:a40",
        "discovery:v100",
        "discovery:p100",
        "endeavour:h200",
        "endeavour:l40s",
        "endeavour:a100",
        "endeavour:a40",
        "endeavour:v100",
        "endeavour:p100",
        "endeavour:rtx5000",
        "laguna:l40s"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = None
    executable = "sleep 1s"
    time_limit = "5m"
    prerun_cmds = [
        "apptainer exec --nv /apps/reframe/resources/containers/gpu-fryer.sif gpu-fryer 120 --nvml-lib-path /.singularity.d/libs/libnvidia-ml.so"
    ]

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--exclusive",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"All GPUs seem healthy", self.stdout)
