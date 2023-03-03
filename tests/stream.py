import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class STREAM(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'STREAM benchmark using gcc/11.3.0'
        self.valid_systems = [
            'discovery:epyc-64',
            'discovery:largemem'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0'
        ]
        self.sourcesdir = None
        self.executable = '/project/hpcroot/reframe2/resources/STREAM/stream_c.exe'
        self.num_tasks = 1
        self.num_cpus_per_task = 64
        self.time_limit = '5m'
        self.variables = {
            'OMP_SCHEDULE': 'static',
            'OMP_DYNAMIC': 'false',
            'OMP_NESTED': 'false',
            'OMP_STACKSIZE': '256M',
            'GOMP_CPU_AFFINITY': '0-63:4',
            'OMP_PROC_BIND': 'true',
            'OMP_NUM_THREADS': '16'
        }
        self.sanity_patterns = sn.assert_found(r'Solution Validates', self.stdout)
        self.perf_patterns = {
            'copy best': sn.extractsingle(r'Copy:\s+(?P<copy_ret>[0-9]+\.[0-9]+)', self.stdout, 'copy_ret', float),
            'scale best': sn.extractsingle(r'Scale:\s+(?P<scale_ret>[0-9]+\.[0-9]+)', self.stdout, 'scale_ret', float),
            'add best': sn.extractsingle(r'Add:\s+(?P<add_ret>[0-9]+\.[0-9]+)', self.stdout, 'add_ret', float),
            'triad best': sn.extractsingle(r'Triad:\s+(?P<triad_ret>[0-9]+\.[0-9]+)', self.stdout, 'triad_ret', float)
        }
        self.reference = {
            '*': {
                'copy best': (300000, -0.10, None, 'MB/s'),
                'scale best': (190000, -0.10, None, 'MB/s'),
                'add best': (210000, -0.10, None, 'MB/s'),
                'triad best': (210000, -0.10, None, 'MB/s')
            }
        }

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--constraint=epyc-7513',
            '--mem=0'
        ]
