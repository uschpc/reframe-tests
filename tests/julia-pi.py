import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Julia_Pi(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Estimating pi using Julia with multiple threads'
        self.valid_systems = [
            'discovery:main',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-julia'
        ]
        self.sourcesdir = './src/julia-pi'
        self.executable = 'julia --threads 4 pi.jl'
        self.num_tasks = 1
        self.num_cpus_per_task = 4
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'3.14', self.stdout)
        self.perf_patterns = {
            'elapsed time': sn.extractsingle(r'Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)', self.stdout, 'elapsed_ret', float)
        }
        self.reference = {
            '*': {
                'elapsed time': (220.0, None, 0.10, 'seconds')
            }
        }
