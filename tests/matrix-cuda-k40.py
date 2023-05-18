import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matrix_CUDA_K40(rfm.RegressionTest):
    def __init__(self):
        self.descr = 'Matrix-vector multiplication example with CUDA using K40'
        self.valid_systems = [
            'discovery:main',
            'discovery:debug'
        ]
        self.valid_prog_environs = [
            'PrgEnv-pgi',
            'PrgEnv-gcc-8.3.0-cuda-10.2.89',
            'PrgEnv-gcc-11.3.0-cuda-11.6.2',
            'PrgEnv-intel-19.0.4-cuda-10.2.89'
        ]
        self.sourcesdir = './src/matrix-cuda'
        self.sourcepath = 'matrix-vector-multiplication-cuda.cu'
        self.build_system = 'SingleSource'
        self.build_system.cxxflags = [
            '-arch=sm_35'
        ]
        self.executable_opts = [
            '10000',
            '10000'
        ]
        self.num_tasks = 1
        self.num_cpus_per_task = 1
        self.time_limit = '10m'
        self.sanity_patterns = sn.assert_found(r'Gflop/s', self.stdout)
        self.perf_patterns = {
            'Gflop/s': sn.extractsingle(r'Performance:\s(?P<gflops_ret>[0-9]+.[0-9]+)', self.stdout, 'gflops_ret', float)
        }
        self.reference = {
            '*': {
                'Gflop/s': (7, -0.10, None, 'gflops')
            }
        }

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--gpus-per-task=k40:1'
        ]