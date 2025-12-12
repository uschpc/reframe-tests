# IOR benchmark test
# For /scratch1 file system
# Purpose of test
# - Test IOR module access
# - Test MPI library
# - Test /scratch1 file system parallel performance
# Notes
# - https://github.com/hpc/ior
# - Other I/O tests for this file system should not be run at the same time
#   because performance results will be negatively impacted

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class ior_scratch1(rfm.RunOnlyRegressionTest):
    descr = "IOR benchmark for /scratch1 file system"
    tags = {
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:epyc-7513",
        "endeavour:epyc-7513"
    ]
    valid_prog_environs = [
        "env-ior"
    ]
    sourcesdir = "src/ior"
    executable = "bash ior.sh scratch1"
    num_tasks = 16
    num_tasks_per_node = 4
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "discovery:epyc-7513": {
            "max_write_speed": (3000, -0.25, None, "MiB/sec"),
            "max_read_speed": (15000, -0.25, None, "MiB/sec")
        },
        "endeavour:epyc-7513": {
            "max_write_speed": (3000, -0.25, None, "MiB/sec"),
            "max_read_speed": (15000, -0.25, None, "MiB/sec")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Finished", self.stdout)

    @performance_function("MiB/sec", perf_key = "max_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"Max Write:\s+(?P<W_ret>\S+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "max_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"Max Read:\s+(?P<R_ret>\S+)", self.stdout, "R_ret", float)
