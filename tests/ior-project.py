import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class IOR_project(rfm.RunOnlyRegressionTest):
    descr = "IOR benchmark for /project file system"
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "laguna:compute"
    ]
    valid_prog_environs = [
        "env-ior"
    ]
    sourcesdir = "src/ior"
    executable = "bash ior.sh project"
    num_tasks = 16
    num_tasks_per_node = 4
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "*": {
            "max_write_speed": (8000.00, -0.25, None, "MiB/sec"),
            "max_read_speed": (18000.00, -0.25, None, "MiB/sec")
        },
        "laguna:compute": {
            "max_write_speed": (7000.00, -0.25, None, "MiB/sec"),
            "max_read_speed": (40000.00, -0.25, None, "MiB/sec")
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
        return sn.assert_found(r"Finished", self.stdout)

    @performance_function("MiB/sec", perf_key = "max_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"Max Write:\s+(?P<W_ret>\S+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "max_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"Max Read:\s+(?P<R_ret>\S+)", self.stdout, "R_ret", float)
