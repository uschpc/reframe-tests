import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class HPL(rfm.RunOnlyRegressionTest):
    descr = 'HPL benchmark using 1 epyc-7513 node'
    valid_systems = [
        'discovery:epyc-64',
        'discovery:main',
        'endeavour:priya',
        'endeavour:qcb'
    ]
    valid_prog_environs = [
        'PrgEnv-hpl'
    ]
    sourcesdir = './src/hpl'
    executable = 'xhpl'
    num_tasks = 64
    num_cpus_per_task = 1
    time_limit = '30m'
    prerun_cmds = [
        'ulimit -s unlimited'
    ]
    env_vars = {
        'OMP_NUM_THREADS': '1',
        'SLURM_MPI_TYPE': 'pmix_v2',
        'SLURM_CPU_BIND': 'verbose'
    }
    reference = {
        '*': {
            'gflops': (2.2, -0.1, None, 'gflops')
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
        return sn.assert_found(r'PASSED', self.stdout)

    @performance_function('gflops', perf_key = 'gflops')
    def extract_perf(self):
        return sn.extractsingle(r'(?P<gflops_ret>[0-9]+.[0-9]+)e\+03$', self.stdout, 'gflops_ret', float)
