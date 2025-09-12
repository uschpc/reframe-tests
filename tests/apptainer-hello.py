# Apptainer test
# Purpose of test
# - Test Apptainer module access
# - Test Apptainer build
# - Test Apptainer exec
# Notes
# - Build from local image file in order to avoid download limits

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class apptainer_hello(rfm.RunOnlyRegressionTest):
    descr = "Apptainer hello world"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "pathfinder:allnodes",
        "laguna:allnodes"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = "src/apptainer"
    executable = "apptainer exec reframe-debian-$SLURM_JOB_ID.sif echo \"Hello world\""
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "cd $TMPDIR",
        "apptainer build --fakeroot reframe-debian-$SLURM_JOB_ID.sif $SLURM_SUBMIT_DIR/debian.def"
    ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Hello world", self.stdout)
