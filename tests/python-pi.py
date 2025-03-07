import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Python_Pi(rfm.RunOnlyRegressionTest):
    descr = "Estimating pi in parallel using Python"
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
        "endeavour:scec",
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-python"
    ]
    sourcesdir = "src/python-pi"
    executable = "python3 pi.py"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    reference = {
        "*": {
            "elapsed_time": (130.0, None, 0.10, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"3.14", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
