import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class IOR_project2(rfm.RunOnlyRegressionTest):
    descr = "IOR benchmark for /project2 file system"
    valid_systems = [
        "discovery:epyc-64",
        "endeavour:qcb"
    ]
    valid_prog_environs = [
        "env-ior"
    ]
    sourcesdir = "src/ior"
    executable = "bash ior.sh project2"
    num_tasks = 16
    num_tasks_per_node = 4
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "*": {
            "max_write_speed": (8000.00, -0.25, None, "MiB/sec"),
            "max_read_speed": (18000.00, -0.25, None, "MiB/sec")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--constraint=epyc-7513"
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
