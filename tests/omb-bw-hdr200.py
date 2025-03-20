import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OMB_BW_HDR200(rfm.RunOnlyRegressionTest):
    descr = "OMB bandwidth benchmark using IB HDR200"
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
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
        "*": {
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
