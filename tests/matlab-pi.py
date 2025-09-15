# MATLAB parallel pi estimation test
# Purpose of test
# - Test MATLAB module access
# - Test MATLAB license access
# - Test MATLAB performance

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class matlab_pi(rfm.RunOnlyRegressionTest):
    descr = "Estimate pi in parallel using MATLAB with parpool"
    tags = {
        "maintenance",
        "performance"
    }
    valid_systems = [
        "discovery:epyc-7542",
        "endeavour:epyc-7513"
    ]
    valid_prog_environs = [
        "env-matlab"
    ]
    sourcesdir = "src/matlab-pi"
    executable = "matlab -batch \"pi\""
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    reference = {
        "discovery:epyc-7542": {
            "elapsed_time": (65.2, None, 0.1, "seconds")
        },
        "endeavour:epyc-7513": {
            "elapsed_time": (52.4, None, 0.1, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"3.14", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
