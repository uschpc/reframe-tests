import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Apptainer_Hello(rfm.RunOnlyRegressionTest):
    descr = "Apptainer hello world"
    valid_systems = [
        "discovery:main",
        "discovery:epyc-64",
        "discovery:gpu",
        "discovery:largemem",
        "discovery:debug",
        "discovery:oneweek",
        "endeavour:shared",
        "endeavour:cryoem",
        "endeavour:isi",
        "endeavour:priya",
        "endeavour:qcb",
        "endeavour:scec"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = None
    executable = "apptainer exec /apps/containers/ood/desktop/rocky8-xfce-desktop-ood3.sif echo \"Hello world\""
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Hello world", self.stdout)
