# Fio random read/write benchmark test
# For /project file system
# Purpose of test
# - Test fio module access
# - Test /project file system access
# - Test /project file system performance
# Notes
# - Other I/O tests for this file system should not be run at the same time
#   because performance results will be negatively impacted

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Fio_randrw_project(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /project file system"
    tags = {
        "maintenance",
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "laguna:compute"
    ]
    valid_prog_environs = [
        "env-fio"
    ]
    sourcesdir = "src/fio-randrw"
    executable = "bash fio-randrw.sh project"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "10m"
    reference = {
        "discovery:allnodes": {
            "avg_write_speed": (75.00, -0.25, None, "MiB/sec"),
            "avg_read_speed": (75.00, -0.25, None, "MiB/sec")
        },
        "endeavour:allnodes": {
            "avg_write_speed": (75.00, -0.25, None, "MiB/sec"),
            "avg_read_speed": (75.00, -0.25, None, "MiB/sec")
        },
        "laguna:compute": {
            "avg_write_speed": (260.00, -0.25, None, "MiB/sec"),
            "avg_read_speed": (260.00, -0.25, None, "MiB/sec")
        }
    }

    @run_before("run")
    def set_job_options(self):
        if self.current_system.name in ["discovery", "endeavour"]:
            self.job.options += [
                "--constraint=epyc-7513"
            ]
        elif self.current_system.name == "laguna":
            self.job.options += [
                "--constraint=epyc-9554"
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
