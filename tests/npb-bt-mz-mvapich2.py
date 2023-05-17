import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_BT_MZ_MVAPICH2(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'NPB BT-MZ MPI+OpenMP benchmark using gcc/11.3.0 and mvapich2/2.3.7 with pmi2'
        self.valid_systems = [
            'discovery:main',
            'discovery:epyc-64',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0-mvapich2-2.3.7'
        ]
        self.sourcesdir = None
        self.executable = '/project/hpcroot/reframe2/resources/NPB/gcc-11.3.0/NPB3.4.2-MZ/NPB3.4-MZ-MPI-mvapich2-2.3.7/bin/bt-mz.A.x'
        self.num_tasks = 4
        self.num_tasks_per_node = 2
        self.num_cpus_per_task = 2
        self.time_limit = '5m'
        self.prerun_cmds = [
            'ulimit -s unlimited'
        ]
        self.env_vars = {
            'OMP_NUM_THREADS': '2',
            'SLURM_MPI_TYPE': 'pmi2',
            'SLURM_CPU_BIND': 'verbose',
            'MV2_USE_RDMA_CM': '0',
            'MV2_HOMOGENEOUS_CLUSTER': '1',
            'MV2_ENABLE_AFFINITY': '0'
        }
        self.sanity_patterns = sn.assert_found(r'SUCCESSFUL', self.stdout)
        self.perf_patterns = {
            'Mop/s total': sn.extractsingle(r'Mop/s total\s+=\s+(?P<mops_ret>\S+)', self.stdout, 'mops_ret', float)
        }
        self.reference = {
            'discovery:main': {
                'Mop/s total': (22000, -0.1, None, 'Mop/s')
            },
            'discovery:epyc-64': {
                'Mop/s total': (46000, -0.1, None, 'Mop/s')
            },
            'endeavour:shared': {
                'Mop/s total': (29000, -0.1, None, 'Mop/s')
            }
        }
