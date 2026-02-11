# NAS Parallel Benchmarks OpenMP MG (multigrid) benchmark test
# Purpose of test
# - Test compiler module access
# - Test building Fortran/OpenMP program
# - Test running Fortran/OpenMP program
# - Test node performance for differential equations solver
#   using multigrid method
# Notes
# - https://www.nas.nasa.gov/software/npb.html
# - Requires a power-of-two number of CPU cores

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_omp_mg(rfm.RunOnlyRegressionTest):
    descr = "NPB OpenMP MG benchmark"
    tags = {
        "maintenance",
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
        "endeavour:epyc-9554-128c",
        "endeavour:epyc-9554-64c",
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
        "pathfinder:xeon-2640v3",
        "laguna:epyc-9554",
        "laguna:epyc-9354"
    ]
    valid_prog_environs = [
        "env-gcc-14.3.0",
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/npb-omp"
    executable = "$TMPDIR/NPB3.4.3/NPB3.4-OMP/bin/mg.D.x"
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_ON_NODE"
    }
    prerun_cmds = [
        "bash make-npb-omp.sh mg D"
    ]
    reference = {
        "discovery:epyc-9534": {
            "Mop/s_total": (106800, -0.1, 0.1, "Mop/s")
        },
        "discovery:epyc-9354": {
            "Mop/s_total": (214000, -0.1, 0.1, "Mop/s")
        },
        "discovery:epyc-7513": {
            "Mop/s_total": (78000, -0.1, 0.1, "Mop/s")
        },
        "discovery:epyc-7313": {
            "Mop/s_total": (80000, -0.1, 0.1, "Mop/s")
        },
        "discovery:epyc-7542": {
            "Mop/s_total": (70600, -0.1, 0.1, "Mop/s")
        },
        "discovery:epyc-7282": {
            "Mop/s_total": (43200, -0.1, 0.1, "Mop/s")
        },
        "discovery:xeon-6130": {
            "Mop/s_total": (57900, -0.1, 0.1, "Mop/s")
        },
        "discovery:xeon-4116": {
            "Mop/s_total": (28000, -0.1, 0.1, "Mop/s")
        },
        "discovery:xeon-2640v4": {
            "Mop/s_total": (27000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-9355": {
            "Mop/s_total": (176900, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-9554-128c": {
            "Mop/s_total": (205600, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-9554-64c": {
            "Mop/s_total": (106900, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-9354": {
            "Mop/s_total": (215000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-9124": {
            "Mop/s_total": (149000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7643": {
            "Mop/s_total": (45000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7513": {
            "Mop/s_total": (78000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7313": {
            "Mop/s_total": (80000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7502": {
            "Mop/s_total": (65000, -0.2, 0.2, "Mop/s")
        },
        "endeavour:epyc-7502p": {
            "Mop/s_total": (37000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-8358": {
            "Mop/s_total": (80000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-6348": {
            "Mop/s_total": (79700, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-6338": {
            "Mop/s_total": (80000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-6226r": {
            "Mop/s_total": (61300, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-6148": {
            "Mop/s_total": (45900, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-6130": {
            "Mop/s_total": (49000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-5118": {
            "Mop/s_total": (34300, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-4116": {
            "Mop/s_total": (39300, -0.1, 0.1, "Mop/s")
        },
        "endeavour:xeon-2640v4": {
            "Mop/s_total": (27900, -0.1, 0.1, "Mop/s")
        },
        "pathfinder:xeon-2640v3": {
            "Mop/s_total": (21400, -0.1, 0.1, "Mop/s")
        },
        "laguna:epyc-9554": {
            "Mop/s_total": (179900, -0.1, 0.1, "Mop/s")
        },
        "laguna:epyc-9354": {
            "Mop/s_total": (193700, -0.1, 0.1, "Mop/s")
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
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
