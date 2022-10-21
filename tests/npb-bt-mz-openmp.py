import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_BT_MZ_OpenMP(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'NPB BT-MZ OpenMP benchmark using gcc/11.3.0'
        self.valid_systems = [
            'discovery:main',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0'
        ]
        self.sourcesdir = None
        self.executable = '/project/hpcroot/reframe2/resources/NPB/gcc-11.3.0/NPB3.4.2-MZ/NPB3.4-MZ-OMP/bin/bt-mz.A.x'
        self.num_tasks = 1
        self.num_cpus_per_task = 8
        self.time_limit = '5m'
        self.variables = {
            'OMP_NUM_THREADS': '4,2',
        }
        self.sanity_patterns = sn.assert_found(r'SUCCESSFUL', self.stdout)
        self.perf_patterns = {
            'Mop/s total': sn.extractsingle(r'Mop/s total\s+=\s+(?P<mops_ret>\S+)', self.stdout, 'mops_ret', float)
        }
        self.reference = {
            '*': {
                'Mop/s total': (23000, -0.1, None, 'Mop/s')
            }
        }
