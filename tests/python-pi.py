# Python parallel pi estimation test
# Purpose of test
# - Test Python module access
# - Test Python performance

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class python_pi(rfm.RunOnlyRegressionTest):
    descr = "Estimating pi in parallel using Python with multiprocessing"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:epyc-7542",
        "endeavour:epyc-7513",
        "pathfinder:xeon-2640v3",
        "laguna:epyc-9554"
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
        "discovery:epyc-7542": {
            "elapsed_time": (100.8, -0.1, 0.1, "seconds")
        },
        "endeavour:epyc-7513": {
            "elapsed_time": (73.8, -0.1, 0.1, "seconds")
        },
        "pathfinder:xeon-2640v3": {
            "elapsed_time": (127.2, -0.1, 0.1, "seconds")
        },
        "laguna:epyc-9554": {
            "elapsed_time": (73.1, -0.1, 0.1, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"3.14", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
