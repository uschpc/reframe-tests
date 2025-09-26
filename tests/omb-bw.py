# OSU Micro Benchmarks bandwidth benchmark test
# Purpose of test
# - Test OSU Micro Benchmarks module access
# - Test running MPI program
# - Test InfiniBand network performance
# Notes
# - Requires exclusive access to nodes in order to
#   have exclusive access to network bandwidth

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class omb_bw(rfm.RunOnlyRegressionTest):
    descr = "OMB bandwidth benchmark"
    tags = {
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:fdr56",
        "discovery:hdr100",
        "discovery:hdr200",
        "discovery:ndr200",
        "endeavour:fdr56",
        "endeavour:hdr100",
        "endeavour:hdr200",
        "endeavour:ndr200",
        "laguna:ndr200"
    ]
    valid_prog_environs = [
        "env-omb"
    ]
    sourcesdir = None
    executable = "osu_get_bw"
    num_tasks = 2
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "discovery:fdr56": {
            "MB/s": (5700, -0.1, None, "MB/s")
        },
        "discovery:hdr100": {
            "MB/s": (11200, -0.1, None, "MB/s")
        },
        "discovery:hdr200": {
            "MB/s": (24600, -0.1, None, "MB/s")
        },
        "discovery:ndr200": {
            "MB/s": (24600, -0.1, None, "MB/s")
        },
        "endeavour:fdr56": {
            "MB/s": (5700, -0.1, None, "MB/s")
        },
        "endeavour:hdr100": {
            "MB/s": (11200, -0.1, None, "MB/s")
        },
        "endeavour:hdr200": {
            "MB/s": (24600, -0.1, None, "MB/s")
        },
        "endeavour:ndr200": {
            "MB/s": (24600, -0.1, None, "MB/s")
        },
        "laguna:ndr200": {
            "MB/s": (24600, -0.1, None, "MB/s")
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

    @performance_function("MB/s", perf_key = "MB/s")
    def extract_perf(self):
        return sn.extractsingle(r"4194304\s+(?P<mbps_ret>\S+)", self.stdout, "mbps_ret", float)
