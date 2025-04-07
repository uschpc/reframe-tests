# Fio random read/write benchmark test
# For /cryoem2 file system
# Purpose of test
# - Test fio module access
# - Test /cryoem2 file system access
# - Test /cryoem2 file system performance
# Notes
# - Other I/O tests for this file system should not be run at the same time
#   because performance results will be negatively impacted

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Fio_randrw_cryoem2(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /cryoem2 file system"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-fio"
    ]
    sourcesdir = "src/fio-randrw"
    executable = "bash fio-randrw.sh cryoem2"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "10m"
    reference = {
        "*": {
            "avg_write_speed": (740.00, -0.25, None, "MiB/sec"),
            "avg_read_speed": (740.00, -0.25, None, "MiB/sec")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--constraint=epyc-7513"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"all jobs", self.stdout)

    @performance_function("MiB/sec", perf_key = "avg_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"WRITE:\sbw=(?P<W_ret>\d+.\d+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "avg_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"READ:\sbw=(?P<R_ret>\d+.\d+)", self.stdout, "R_ret", float)
