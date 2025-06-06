# STREAM benchmark test
# For EPYC 7542 nodes
# Purpose of test
# - Test compiler module access
# - Test building C/OpenMP program
# - Test running C/OpenMP program
# - Test memory bandwidth performance for EPYC 7542 nodes

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class STREAM_EPYC_7542(rfm.RunOnlyRegressionTest):
    descr = "STREAM benchmark for EPYC 7542 nodes"
    tags = {
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:main",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/stream"
    executable = "stream_c.exe"
    num_tasks = 1
    num_cpus_per_task = 64
    time_limit = "5m"
    env_vars = {
        "OMP_SCHEDULE": "static",
        "OMP_DYNAMIC": "false",
        "OMP_NESTED": "false",
        "OMP_PROC_BIND": "true",
        "OMP_PLACES": "0:16:4",
        "OMP_NUM_THREADS": "16"
    }
    prerun_cmds = [
        "bash make-stream.sh"
    ]
    reference = {
        "*": {
            "copy_best": (278000, -0.1, None, "MB/s"),
            "scale_best": (172000, -0.1, None, "MB/s"),
            "add_best": (190000, -0.1, None, "MB/s"),
            "triad_best": (190000, -0.1, None, "MB/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--constraint=epyc-7542",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Solution Validates", self.stdout)

    @performance_function("MB/s", perf_key = "copy_best")
    def extract_perf_copy(self):
        return sn.extractsingle(r"Copy:\s+(?P<copy_ret>[0-9]+\.[0-9]+)", self.stdout, "copy_ret", float)

    @performance_function("MB/s", perf_key = "scale_best")
    def extract_perf_scale(self):
        return sn.extractsingle(r"Scale:\s+(?P<scale_ret>[0-9]+\.[0-9]+)", self.stdout, "scale_ret", float)

    @performance_function("MB/s", perf_key = "add_best")
    def extract_perf_add(self):
        return sn.extractsingle(r"Add:\s+(?P<add_ret>[0-9]+\.[0-9]+)", self.stdout, "add_ret", float)

    @performance_function("MB/s", perf_key = "triad_best")
    def extract_perf_triad(self):
        return sn.extractsingle(r"Triad:\s+(?P<triad_ret>[0-9]+\.[0-9]+)", self.stdout, "triad_ret", float)
