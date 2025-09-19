# R parallel bootstrap test
# Purpose of test
# - Test R module access
# - Test R performance

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class r_bootstrap(rfm.RunOnlyRegressionTest):
    descr = "Bootstrapping a GLM in parallel using R with mclapply"
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
        "env-r"
    ]
    sourcesdir = "src/r-bootstrap"
    executable = "Rscript bootstrap.R"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    reference = {
        "discovery:epyc-7542": {
            "elapsed_time": (95.9, None, 0.1, "seconds")
        },
        "endeavour:epyc-7513": {
            "elapsed_time": (79.9, None, 0.1, "seconds")
        },
        "pathfinder:xeon-2640v3": {
            "elapsed_time": (190.5, None, 0.1, "seconds")
        },
        "laguna:epyc-9554": {
            "elapsed_time": (62.7, None, 0.1, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Elapsed time", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
