# Apptainer GPU test
# Purpose of test
# - Test Apptainer module access
# - Test Apptainer build
# - Test Apptainer exec
# - Test Apptainer GPU access
# Notes
# - Build from local image file in order to avoid download limits

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Apptainer_GPU_Hello(rfm.RunOnlyRegressionTest):
    descr = "Apptainer GPU access"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = "src/apptainer"
    executable = "apptainer exec --nv debian.sif echo \"Hello world from $(nvidia-smi -L)\""
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "cd $TMPDIR",
        "apptainer build --fakeroot debian.sif $SLURM_SUBMIT_DIR/debian.def"
    ]

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"UUID", self.stdout)
