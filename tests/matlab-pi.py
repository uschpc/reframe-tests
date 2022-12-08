import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matlab_Pi(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Estimate pi using a Matlab parpool'
        self.valid_systems = [
            'discovery:main',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-matlab'
        ]
        self.sourcesdir = './src/matlab-pi'
        self.executable = 'matlab -batch \'pi\''
        self.num_tasks = 1
        self.num_cpus_per_task = 4
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'3.14', self.stdout)
        self.perf_patterns = {
            'elapsed time': sn.extractsingle(r'Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)', self.stdout, 'elapsed_ret', float)
        }
        self.reference = {
            '*': {
                'elapsed time': (175.0, None, 0.10, 'seconds')
            }
        }
