import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_BT_OpenMPI(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'NPB BT MPI benchmark using gcc/11.3.0 and openmpi/4.1.4 with pmix_v2'
        self.valid_systems = [
            'discovery:main',
            'discovery:epyc-64',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0-openmpi-4.1.4'
        ]
        self.sourcesdir = None
        self.executable = '/project/hpcroot/reframe2/resources/NPB/gcc-11.3.0/NPB3.4.2/NPB3.4-MPI-openmpi-4.1.4/bin/bt.A.x'
        self.num_tasks = 4
        self.num_tasks_per_node = 2
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.prerun_cmds = [
            'ulimit -s unlimited'
        ]
        self.env_vars = {
            'OMP_NUM_THREADS': '1',
            'SLURM_MPI_TYPE': 'pmix_v2',
            'SLURM_CPU_BIND': 'verbose'
        }
        self.sanity_patterns = sn.assert_found(r'SUCCESSFUL', self.stdout)
        self.perf_patterns = {
            'Mop/s total': sn.extractsingle(r'Mop/s total\s+=\s+(?P<mops_ret>\S+)', self.stdout, 'mops_ret', float)
        }
        self.reference = {
            'discovery:main': {
                'Mop/s total': (11000, -0.1, None, 'Mop/s')
            },
            'discovery:epyc-64': {
                'Mop/s total': (22500, -0.1, None, 'Mop/s')
            },
            'endeavour:shared': {
                'Mop/s total': (9000, -0.1, None, 'Mop/s')
            }
        }
