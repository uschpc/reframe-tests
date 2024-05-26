import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class STREAM(rfm.RunOnlyRegressionTest):
    descr = 'STREAM benchmark using gcc/11.3.0'
    valid_systems = [
        'discovery:epyc-64',
        'discovery:gpu',
        'discovery:largemem',
        'endeavour:priya',
        'endeavour:qcb'
    ]
    valid_prog_environs = [
        'PrgEnv-gcc-11.3.0'
    ]
    sourcesdir = None
    executable = '/project/hpcroot/rfm/resources/STREAM/stream_c.exe'
    num_tasks = 1
    num_cpus_per_task = 64
    time_limit = '5m'
    env_vars = {
        'OMP_SCHEDULE': 'static',
        'OMP_DYNAMIC': 'false',
        'OMP_NESTED': 'false',
        'OMP_STACKSIZE': '256M',
        'GOMP_CPU_AFFINITY': '0-63:4',
        'OMP_PROC_BIND': 'true',
        'OMP_NUM_THREADS': '16'
    }
    reference = {
        '*': {
            'copy_best': (300000, -0.10, None, 'MB/s'),
            'scale_best': (190000, -0.10, None, 'MB/s'),
            'add_best': (210000, -0.10, None, 'MB/s'),
            'triad_best': (210000, -0.10, None, 'MB/s')
        }
    }

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--constraint=epyc-7513',
            '--mem=0'
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'Solution Validates', self.stdout)

    @performance_function('MB/s', perf_key = 'copy_best')
    def extract_perf_copy(self):
        return sn.extractsingle(r'Copy:\s+(?P<copy_ret>[0-9]+\.[0-9]+)', self.stdout, 'copy_ret', float)

    @performance_function('MB/s', perf_key = 'scale_best')
    def extract_perf_scale(self):
        return sn.extractsingle(r'Scale:\s+(?P<scale_ret>[0-9]+\.[0-9]+)', self.stdout, 'scale_ret', float)

    @performance_function('MB/s', perf_key = 'add_best')
    def extract_perf_add(self):
        return sn.extractsingle(r'Add:\s+(?P<add_ret>[0-9]+\.[0-9]+)', self.stdout, 'add_ret', float)

    @performance_function('MB/s', perf_key = 'triad_best')
    def extract_perf_triad(self):
        return sn.extractsingle(r'Triad:\s+(?P<triad_ret>[0-9]+\.[0-9]+)', self.stdout, 'triad_ret', float)
