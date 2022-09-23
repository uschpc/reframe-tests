import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class RBootstrap(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Bootstrapping a GLM in parallel using R'
        self.tags = {
            'daily'
        }
        self.valid_systems = [
            'discovery:main',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-R'
        ]
        self.sourcesdir = './src/r-bootstrap'
        self.executable = 'Rscript bootstrap.R'
        self.num_tasks = 1
        self.num_cpus_per_task = 8
        self.time_limit = '5m'
        self.variables = {
            'OMP_NUM_THREADS': '1'
        }
        self.sanity_patterns = sn.assert_found(r'Elapsed time', self.stdout)
        self.perf_patterns = {
            'elapsed time': sn.extractsingle(r'Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)', self.stdout, 'elapsed_ret', float)
        }
        self.reference = {
            '*': {
                'elapsed time': (210.0, None, 0.25, 'seconds')
            }
        }
