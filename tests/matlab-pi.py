import math
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
        self.num_cpus_per_task = 8
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'pi\s=', self.stdout)
        self.perf_patterns = {
            'pi estimate': sn.extractsingle(r'pi\s=\s(?P<pi_ret>[0-9]\.[0-9]+)', self.stdout, 'pi_ret', float)
        }
        self.reference = {
            '*': {
                'pi estimate': (math.pi, -0.05, 0.05, None)
            }
        }
