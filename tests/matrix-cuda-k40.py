import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matrix_CUDA_K40(rfm.RegressionTest):
    descr = "Matrix-vector multiplication example with CUDA using K40"
    valid_systems = [
        "discovery:main"
    ]
    valid_prog_environs = [
        "PrgEnv-gcc-8.3.0-cuda-10.2.89",
        "PrgEnv-gcc-11.3.0-cuda-11.6.2"
    ]
    sourcesdir = "./src/matrix-cuda"
    sourcepath = "matrix-vector-multiplication-cuda.cu"
    build_system = "SingleSource"
    executable_opts = [
        "10000",
        "10000"
    ]
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "10m"
    reference = {
        "*": {
            "gflops": (7, -0.10, None, "gflops")
        }
    }

    @run_before("compile")
    def set_compiler_flags(self):
        self.build_system.cxxflags = [
            "-arch=sm_35"
        ]

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=k40:1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Gflop/s", self.stdout)

    @performance_function("gflops", perf_key = "gflops")
    def extract_perf(self):
        return sn.extractsingle(r"Performance:\s(?P<gflops_ret>[0-9]+.[0-9]+)", self.stdout, "gflops_ret", float)
