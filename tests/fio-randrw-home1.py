import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Fio_randrw_home1(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /home1 file system"
    tags = {
        "maintenance"
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
    executable = "bash fio-randrw.sh home1"
    num_tasks = 1
    num_cpus_per_task = 4
    time_limit = "5m"
    reference = {
        "*": {
            "avg_write_speed": (65.00, -0.1, None, "MiB/sec"),
            "avg_read_speed": (65.00, -0.1, None, "MiB/sec")
        },
        "laguna:compute": {
            "avg_write_speed": (72.00, -0.1, None, "MiB/sec"),
            "avg_read_speed": (72.00, -0.1, None, "MiB/sec")
        }
    }

    @run_before("run")
    def set_job_options(self):
        if self.current_partition.name in ["epyc-64", "qcb"]:
            self.job.options += [
                "--constraint=epyc-7513"
            ]
        elif self.current_partition.name == "compute":
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
