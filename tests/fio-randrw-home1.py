# Fio random read/write benchmark test
# For /home1 file system
# Purpose of test
# - Test fio module access
# - Test /home1 file system access
# - Test /home1 file system performance
# Notes
# - Other I/O tests for this file system should not be run at the same time
#   because performance results will be negatively impacted

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class fio_randrw_home1(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /home1 file system"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:epyc-7513",
        "endeavour:epyc-9554",
        "laguna:epyc-9554"
    ]
    valid_prog_environs = [
        "env-fio"
    ]
    sourcesdir = "src/fio-randrw"
    executable = "bash fio-randrw.sh home1"
    num_tasks = 1
    num_cpus_per_task = 4
    time_limit = "5m"
    reference = {
        "discovery:epyc-7513": {
            "avg_write_speed": (75, -0.1, None, "MiB/sec"),
            "avg_read_speed": (75, -0.1, None, "MiB/sec")
        },
        "endeavour:epyc-9554": {
            "avg_write_speed": (83, -0.1, None, "MiB/sec"),
            "avg_read_speed": (83, -0.1, None, "MiB/sec")
        },
        "laguna:epyc-9554": {
            "avg_write_speed": (72, -0.1, None, "MiB/sec"),
            "avg_read_speed": (72, -0.1, None, "MiB/sec")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"all jobs", self.stdout)

    @performance_function("MiB/sec", perf_key = "avg_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"WRITE:\sbw=(?P<W_ret>\d+.\d+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "avg_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"READ:\sbw=(?P<R_ret>\d+.\d+)", self.stdout, "R_ret", float)
