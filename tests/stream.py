# STREAM benchmark test
# Purpose of test
# - Test compiler module access
# - Test building C/OpenMP program
# - Test running C/OpenMP program
# - Test memory bandwidth performance

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class stream(rfm.RunOnlyRegressionTest):
    descr = "STREAM benchmark"
    tags = {
        "performance",
        "singlenode"
    }
    valid_systems = [
        "discovery:epyc-9534",
        "discovery:epyc-9354",
        "discovery:epyc-7513",
        "discovery:epyc-7313",
        "discovery:epyc-7542",
        "endeavour:epyc-9554",
        "endeavour:epyc-9354",
        "endeavour:epyc-7513",
        "endeavour:epyc-7313",
        "laguna:epyc-9554",
        "laguna:epyc-9354"
    ]
    valid_prog_environs = [
        "env-gcc-14.3.0",
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/stream"
    executable = "stream_c.exe"
    num_tasks = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-stream.sh",
        "source set-omp-vars.sh"
    ]
    reference = {
        "discovery:epyc-9534": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (472000, -0.1, 0.1, "MB/s"),
            "add_best": (527000, -0.1, 0.1, "MB/s"),
            "triad_best": (528000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-9354": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (472000, -0.1, 0.1, "MB/s"),
            "add_best": (527000, -0.1, 0.1, "MB/s"),
            "triad_best": (528000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7513": {
            "copy_best": (300000, -0.1, 0.1, "MB/s"),
            "scale_best": (190000, -0.1, 0.1, "MB/s"),
            "add_best": (210000, -0.1, 0.1, "MB/s"),
            "triad_best": (210000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7313": {
            "copy_best": (150000, -0.1, 0.1, "MB/s"),
            "scale_best": (100000, -0.1, 0.1, "MB/s"),
            "add_best": (110000, -0.1, 0.1, "MB/s"),
            "triad_best": (110000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7542": {
            "copy_best": (278000, -0.1, 0.1, "MB/s"),
            "scale_best": (172000, -0.1, 0.1, "MB/s"),
            "add_best": (190000, -0.1, 0.1, "MB/s"),
            "triad_best": (190000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9554": {
            "copy_best": (617000, -0.1, 0.1, "MB/s"),
            "scale_best": (418000, -0.1, 0.1, "MB/s"),
            "add_best": (473000, -0.1, 0.1, "MB/s"),
            "triad_best": (474000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9354": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (472000, -0.1, 0.1, "MB/s"),
            "add_best": (527000, -0.1, 0.1, "MB/s"),
            "triad_best": (528000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7513": {
            "copy_best": (300000, -0.1, 0.1, "MB/s"),
            "scale_best": (190000, -0.1, 0.1, "MB/s"),
            "add_best": (210000, -0.1, 0.1, "MB/s"),
            "triad_best": (210000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7313": {
            "copy_best": (150000, -0.1, 0.1, "MB/s"),
            "scale_best": (100000, -0.1, 0.1, "MB/s"),
            "add_best": (110000, -0.1, 0.1, "MB/s"),
            "triad_best": (110000, -0.1, 0.1, "MB/s")
        },
        "laguna:epyc-9554": {
            "copy_best": (617000, -0.1, 0.1, "MB/s"),
            "scale_best": (418000, -0.1, 0.1, "MB/s"),
            "add_best": (473000, -0.1, 0.1, "MB/s"),
            "triad_best": (474000, -0.1, 0.1, "MB/s")
        },
        "laguna:epyc-9354": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (472000, -0.1, 0.1, "MB/s"),
            "add_best": (527000, -0.1, 0.1, "MB/s"),
            "triad_best": (528000, -0.1, 0.1, "MB/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--exclusive",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Solution Validates", self.stdout)

    @performance_function("MB/s", perf_key = "copy_best")
    def extract_perf_copy(self):
        return sn.extractsingle(r"Copy:\s+(?P<copy_ret>[0-9]+\.[0-9]+)", self.stdout, "copy_ret", float)

    @performance_function("MB/s", perf_key = "scale_best")
    def extract_perf_scale(self):
        return sn.extractsingle(r"Scale:\s+(?P<scale_ret>[0-9]+\.[0-9]+)", self.stdout, "scale_ret", float)

    @performance_function("MB/s", perf_key = "add_best")
    def extract_perf_add(self):
        return sn.extractsingle(r"Add:\s+(?P<add_ret>[0-9]+\.[0-9]+)", self.stdout, "add_ret", float)

    @performance_function("MB/s", perf_key = "triad_best")
    def extract_perf_triad(self):
        return sn.extractsingle(r"Triad:\s+(?P<triad_ret>[0-9]+\.[0-9]+)", self.stdout, "triad_ret", float)
