import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_OMP_MG(rfm.RunOnlyRegressionTest):
    descr = "NPB OpenMP MG benchmark"
    valid_systems = [
        "discovery:main",
        "discovery:epyc-64",
        "discovery:gpu",
        "discovery:largemem",
        "discovery:debug",
        "discovery:oneweek",
        "endeavour:shared",
        "endeavour:cryoem",
        "endeavour:isi",
        "endeavour:priya",
        "endeavour:qcb",
        "endeavour:scec"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    sourcesdir = "src/npb-omp-mg"
    executable = "NPB3.4.3/NPB3.4-OMP/bin/mg.D.x"
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_ON_NODE"
    }
    prerun_cmds = [
        "bash make-npb-omp-mg.sh"
    ]
    reference = {
        "discovery:main": {
            "Mop/s_total": (30000, -0.1, None, "Mop/s")
        },
        "discovery:epyc-64": {
            "Mop/s_total": (70000, -0.1, None, "Mop/s")
        },
        "discovery:gpu": {
            "Mop/s_total": (21000, -0.1, None, "Mop/s")
        },
        "discovery:largemem": {
            "Mop/s_total": (70000, -0.1, None, "Mop/s")
        },
        "discovery:debug": {
            "Mop/s_total": (21000, -0.1, None, "Mop/s")
        },
        "discovery:oneweek": {
            "Mop/s_total": (30000, -0.1, None, "Mop/s")
        },
        "endeavour:shared": {
            "Mop/s_total": (30000, -0.1, None, "Mop/s")
        },
        "endeavour:cryoem": {
            "Mop/s_total": (21000, -0.1, None, "Mop/s")
        },
        "endeavour:isi": {
            "Mop/s_total": (21000, -0.1, None, "Mop/s")
        },
        "endeavour:priya": {
            "Mop/s_total": (70000, -0.1, None, "Mop/s")
        },
        "endeavour:qcb": {
            "Mop/s_total": (30000, -0.1, None, "Mop/s")
        },
        "endeavour:scec": {
            "Mop/s_total": (21000, -0.1, None, "Mop/s")
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
        return sn.assert_found(r"VERIFICATION SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
