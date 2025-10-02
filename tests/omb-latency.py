# OSU Micro Benchmarks latency benchmark test
# Purpose of test
# - Test OSU Micro Benchmarks module access
# - Test running MPI program
# - Test InfiniBand network latency performance
# Notes
# - Requires exclusive access to nodes in order to
#   have exclusive access to NICs

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class omb_latency(rfm.RunOnlyRegressionTest):
    descr = "OMB latency benchmark"
    tags = {
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:ndr200",
        "discovery:hdr200",
        "discovery:hdr100",
        "discovery:fdr56",
        "endeavour:ndr200",
        "endeavour:hdr200",
        "endeavour:hdr100",
        "endeavour:fdr56",
        "laguna:ndr200"
    ]
    valid_prog_environs = [
        "env-omb"
    ]
    sourcesdir = None
    executable = "osu_latency"
    num_tasks = 2
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "discovery:ndr200": {
            "us": (173, -0.05, 0.05, "us")
        },
        "discovery:hdr200": {
            "us": (177, -0.05, 0.05, "us")
        },
        "discovery:hdr100": {
            "us": (352, -0.05, 0.05, "us")
        },
        "discovery:fdr56": {
            "us": (664, -0.05, 0.05, "us")
        },
        "endeavour:ndr200": {
            "us": (173, -0.05, 0.05, "us")
        },
        "endeavour:hdr200": {
            "us": (177, -0.05, 0.05, "us")
        },
        "endeavour:hdr100": {
            "us": (352, -0.05, 0.05, "us")
        },
        "endeavour:fdr56": {
            "us": (664, -0.05, 0.05, "us")
        },
        "laguna:ndr200": {
            "us": (173, -0.05, 0.05, "us")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"4194304", self.stdout)

    @performance_function("us", perf_key = "us")
    def extract_perf(self):
        return sn.extractsingle(r"4194304\s+(?P<us_ret>\S+)", self.stdout, "us_ret", float)
