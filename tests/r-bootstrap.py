import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class R_Bootstrap(rfm.RunOnlyRegressionTest):
    descr = "Bootstrapping a GLM in parallel using R"
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
        "env-R"
    ]
    sourcesdir = "./src/r-bootstrap"
    executable = "Rscript bootstrap.R"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "1"
    }
    reference = {
        "discovery:main": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "discovery:epyc-64": {
            "elapsed_time": (115.0, None, 0.25, "seconds")
        },
        "discovery:gpu": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "discovery:largemem": {
            "elapsed_time": (90.0, None, 0.25, "seconds")
        },
        "discovery:debug": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "discovery:oneweek": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:shared": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:cryoem": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:isi": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:priya": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:qcb": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        },
        "endeavour:scec": {
            "elapsed_time": (170.0, None, 0.25, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Elapsed time", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
