# STREAM benchmark test
# Purpose of test
# - Test compiler module access
# - Test building C/OpenMP program
# - Test running C/OpenMP program
# - Test memory bandwidth performance
# Notes
# - https://github.com/jeffhammond/STREAM

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
        "discovery:epyc-7282",
        "discovery:xeon-6130",
        "discovery:xeon-4116",
        "discovery:xeon-2640v4",
        "endeavour:epyc-9355",
        "endeavour:epyc-9554-2s",
        "endeavour:epyc-9554-1s",
        "endeavour:epyc-9354",
        "endeavour:epyc-9124",
        "endeavour:epyc-7643",
        "endeavour:epyc-7513",
        "endeavour:epyc-7313",
        "endeavour:epyc-7502",
        "endeavour:epyc-7502p",
        "endeavour:xeon-8358",
        "endeavour:xeon-6348",
        "endeavour:xeon-6338",
        "endeavour:xeon-6226r",
        "endeavour:xeon-6148",
        "endeavour:xeon-6130",
        "endeavour:xeon-5118",
        "endeavour:xeon-4116",
        "endeavour:xeon-2640v4",
        "laguna:epyc-9554",
        "laguna:epyc-9354"
    ]
    valid_prog_environs = [
        "env-gcc-14.3.0",
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/stream"
    executable = "$TMPDIR/STREAM/stream_c.exe"
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
            "copy_best": (318000, -0.1, 0.1, "MB/s"),
            "scale_best": (219000, -0.1, 0.1, "MB/s"),
            "add_best": (240000, -0.1, 0.1, "MB/s"),
            "triad_best": (240000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7313": {
            "copy_best": (308000, -0.1, 0.1, "MB/s"),
            "scale_best": (188000, -0.1, 0.1, "MB/s"),
            "add_best": (206000, -0.1, 0.1, "MB/s"),
            "triad_best": (206000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7542": {
            "copy_best": (278000, -0.1, 0.1, "MB/s"),
            "scale_best": (172000, -0.1, 0.1, "MB/s"),
            "add_best": (190000, -0.1, 0.1, "MB/s"),
            "triad_best": (190000, -0.1, 0.1, "MB/s")
        },
        "discovery:epyc-7282": {
            "copy_best": (155000, -0.1, 0.1, "MB/s"),
            "scale_best": (101000, -0.1, 0.1, "MB/s"),
            "add_best": (110000, -0.1, 0.1, "MB/s"),
            "triad_best": (110000, -0.1, 0.1, "MB/s")
        },
        "discovery:xeon-6130": {
            "copy_best": (145000, -0.1, 0.1, "MB/s"),
            "scale_best": (108000, -0.1, 0.1, "MB/s"),
            "add_best": (121000, -0.1, 0.1, "MB/s"),
            "triad_best": (121000, -0.1, 0.1, "MB/s")
        },
        "discovery:xeon-4116": {
            "copy_best": (124000, -0.1, 0.1, "MB/s"),
            "scale_best": (94000, -0.1, 0.1, "MB/s"),
            "add_best": (106000, -0.1, 0.1, "MB/s"),
            "triad_best": (106000, -0.1, 0.1, "MB/s")
        },
        "discovery:xeon-2640v4": {
            "copy_best": (77000, -0.1, 0.1, "MB/s"),
            "scale_best": (65000, -0.1, 0.1, "MB/s"),
            "add_best": (71000, -0.1, 0.1, "MB/s"),
            "triad_best": (71000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9355": {
            "copy_best": (975000, -0.1, 0.1, "MB/s"),
            "scale_best": (667000, -0.1, 0.1, "MB/s"),
            "add_best": (755000, -0.1, 0.1, "MB/s"),
            "triad_best": (755000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9554-2s": {
            "copy_best": (617000, -0.1, 0.1, "MB/s"),
            "scale_best": (418000, -0.1, 0.1, "MB/s"),
            "add_best": (473000, -0.1, 0.1, "MB/s"),
            "triad_best": (474000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9554-1s": {
            "copy_best": (617000, -0.1, 0.1, "MB/s"),
            "scale_best": (418000, -0.1, 0.1, "MB/s"),
            "add_best": (473000, -0.1, 0.1, "MB/s"),
            "triad_best": (474000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9354": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (485000, -0.1, 0.1, "MB/s"),
            "add_best": (546000, -0.1, 0.1, "MB/s"),
            "triad_best": (544000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-9124": {
            "copy_best": (441000, -0.1, 0.1, "MB/s"),
            "scale_best": (377000, -0.1, 0.1, "MB/s"),
            "add_best": (403000, -0.1, 0.1, "MB/s"),
            "triad_best": (402000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7643": {
            "copy_best": (156000, -0.1, 0.1, "MB/s"),
            "scale_best": (104000, -0.1, 0.1, "MB/s"),
            "add_best": (115000, -0.1, 0.1, "MB/s"),
            "triad_best": (115000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7513": {
            "copy_best": (318000, -0.1, 0.1, "MB/s"),
            "scale_best": (219000, -0.1, 0.1, "MB/s"),
            "add_best": (240000, -0.1, 0.1, "MB/s"),
            "triad_best": (240000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7313": {
            "copy_best": (308000, -0.1, 0.1, "MB/s"),
            "scale_best": (188000, -0.1, 0.1, "MB/s"),
            "add_best": (206000, -0.1, 0.1, "MB/s"),
            "triad_best": (206000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7502": {
            "copy_best": (278000, -0.1, 0.1, "MB/s"),
            "scale_best": (169000, -0.1, 0.1, "MB/s"),
            "add_best": (188000, -0.1, 0.1, "MB/s"),
            "triad_best": (188000, -0.1, 0.1, "MB/s")
        },
        "endeavour:epyc-7502p": {
            "copy_best": (139000, -0.1, 0.1, "MB/s"),
            "scale_best": (84600, -0.1, 0.1, "MB/s"),
            "add_best": (94000, -0.1, 0.1, "MB/s"),
            "triad_best": (94000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-8358": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (485000, -0.1, 0.1, "MB/s"),
            "add_best": (546000, -0.1, 0.1, "MB/s"),
            "triad_best": (544000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-6348": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (485000, -0.1, 0.1, "MB/s"),
            "add_best": (546000, -0.1, 0.1, "MB/s"),
            "triad_best": (544000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-6338": {
            "copy_best": (703000, -0.1, 0.1, "MB/s"),
            "scale_best": (485000, -0.1, 0.1, "MB/s"),
            "add_best": (546000, -0.1, 0.1, "MB/s"),
            "triad_best": (544000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-6226r": {
            "copy_best": (184000, -0.1, 0.1, "MB/s"),
            "scale_best": (140000, -0.1, 0.1, "MB/s"),
            "add_best": (159000, -0.1, 0.1, "MB/s"),
            "triad_best": (159000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-6148": {
            "copy_best": (164000, -0.1, 0.1, "MB/s"),
            "scale_best": (120000, -0.1, 0.1, "MB/s"),
            "add_best": (137000, -0.1, 0.1, "MB/s"),
            "triad_best": (137000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-6130": {
            "copy_best": (145000, -0.1, 0.1, "MB/s"),
            "scale_best": (108000, -0.1, 0.1, "MB/s"),
            "add_best": (121000, -0.1, 0.1, "MB/s"),
            "triad_best": (121000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-5118": {
            "copy_best": (112000, -0.1, 0.1, "MB/s"),
            "scale_best": (81000, -0.1, 0.1, "MB/s"),
            "add_best": (91000, -0.1, 0.1, "MB/s"),
            "triad_best": (91000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-4116": {
            "copy_best": (124000, -0.1, 0.1, "MB/s"),
            "scale_best": (94000, -0.1, 0.1, "MB/s"),
            "add_best": (106000, -0.1, 0.1, "MB/s"),
            "triad_best": (106000, -0.1, 0.1, "MB/s")
        },
        "endeavour:xeon-2640v4": {
            "copy_best": (77000, -0.1, 0.1, "MB/s"),
            "scale_best": (65000, -0.1, 0.1, "MB/s"),
            "add_best": (71000, -0.1, 0.1, "MB/s"),
            "triad_best": (71000, -0.1, 0.1, "MB/s")
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
