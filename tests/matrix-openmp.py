import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matrix_OpenMP(rfm.RegressionTest):
    descr = "Matrix-vector multiplication example using OpenMP"
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
        "env-gcc-11.3.0",
        "env-gcc-12.3.0"
    ]
    sourcesdir = "./src/matrix-openmp"
    sourcepath = "matrix-vector-multiplication-openmp.c"
    executable_opts = [
        "4200",
        "10000"
    ]
    build_system = "SingleSource"
    num_tasks = 1
    num_cpus_per_task = 4
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "4"
    }
    reference = {
        "*": {
            "elapsed_time": (1.8, None, 0.25, "seconds")
        }
    }

    @run_before("compile")
    def set_compiler_flags(self):
        self.build_system.cflags = [
            "-fopenmp"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"time for single matrix vector multiplication", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"multiplication\s(?P<time_ret>[0-9]+.[0-9]+)", self.stdout, "time_ret", float)
