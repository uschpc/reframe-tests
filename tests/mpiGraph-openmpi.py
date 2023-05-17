import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class mpiGraph_OpenMPI(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'mpiGraph benchmark using gcc/11.3.0 and openmpi/4.1.4 with pmix_v2'
        self.valid_systems = [
            'discovery:main',
            'discovery:epyc-64',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0-openmpi-4.1.4'
        ]
        self.sourcesdir = None
        self.executable = '/project/hpcroot/reframe2/resources/mpiGraph/gcc-11.3.0-openmpi-4.1.4/mpiGraph 1048576 10 10'
        self.num_tasks = 8
        self.num_tasks_per_node = 1
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.prerun_cmds = [
            'ulimit -s unlimited'
        ]
        self.env_vars = {
            'SLURM_MPI_TYPE': 'pmix_v2',
            'SLURM_CPU_BIND': 'verbose'
        }
        self.sanity_patterns = sn.assert_found(r'END mpiGraph', self.stdout)
        self.perf_patterns = {
            'send avg': sn.extractsingle(r'Send avg\s+(?P<S_ret>[0-9]+\.[0-9]+)', self.stdout, 'S_ret', float),
            'recv avg': sn.extractsingle(r'Recv avg\s+(?P<R_ret>[0-9]+\.[0-9]+)', self.stdout, 'R_ret', float)
        }
        self.reference = {
            'discovery:main': {
                'send avg': (3000, -0.10, None, 'msg bandwidth'),
                'recv avg': (3000, -0.10, None, 'msg bandwidth')
            },
            'discovery:epyc-64': {
                'send avg': (5000, -0.10, None, 'msg bandwidth'),
                'recv avg': (5000, -0.10, None, 'msg bandwidth')
            },
            'endeavour:shared': {
                'send avg': (3700, -0.10, None, 'msg bandwidth'),
                'recv avg': (3700, -0.10, None, 'msg bandwidth')
            }
        }
