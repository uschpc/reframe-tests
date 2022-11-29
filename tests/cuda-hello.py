import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class CUDA_Hello(rfm.RegressionTest):
    def __init__(self):
        self.descr = 'CUDA hello world'
        self.valid_systems = [
            'discovery:gpu'
        ]
        self.valid_prog_environs = [
            'PrgEnv-pgi',
            'PrgEnv-gcc-8.3.0-cuda-10.2.89',
            'PrgEnv-gcc-11.3.0-cuda-11.6.2',
            'PrgEnv-intel-19.0.4-cuda-10.2.89'
        ]
        self.sourcesdir = './src/cuda-hello'
        self.sourcepath = 'hello.cu'
        self.build_system = 'SingleSource'
        self.num_tasks = 1
        self.num_cpus_per_task = 2
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'Hello World!', self.stdout)

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--gres=gpu:p100:1',
            '--gres-flags=enforce-binding'
        ]
