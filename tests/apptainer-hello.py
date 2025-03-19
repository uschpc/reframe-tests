import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Apptainer_Hello(rfm.RunOnlyRegressionTest):
    descr = "Apptainer hello world"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = "src/apptainer"
    executable = "apptainer exec debian.sif echo \"Hello world\""
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "cd $TMPDIR",
        "apptainer build --fakeroot debian.sif $SLURM_SUBMIT_DIR/debian.def"
    ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Hello world", self.stdout)
