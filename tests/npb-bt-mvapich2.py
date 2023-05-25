import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_BT_MVAPICH2(rfm.RunOnlyRegressionTest):
    descr = 'NPB BT MPI benchmark using gcc/11.3.0 and mvapich2/2.3.7 with pmi2'
    valid_systems = [
        'discovery:main',
        'discovery:epyc-64',
        'discovery:gpu',
        'endeavour:shared'
    ]
    valid_prog_environs = [
        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7'
    ]
    sourcesdir = None
    executable = '/project/hpcroot/reframe2/resources/NPB/gcc-11.3.0/NPB3.4.2/NPB3.4-MPI-mvapich2-2.3.7/bin/bt.A.x'
    num_tasks = 4
    num_tasks_per_node = 2
    num_cpus_per_task = 1
    time_limit = '5m'
    prerun_cmds = [
        'ulimit -s unlimited'
    ]
    env_vars = {
        'OMP_NUM_THREADS': '1',
        'SLURM_MPI_TYPE': 'pmi2',
        'SLURM_CPU_BIND': 'verbose',
        'MV2_USE_RDMA_CM': '0',
        'MV2_HOMOGENEOUS_CLUSTER': '1',
        'MV2_ENABLE_AFFINITY': '1'
    }
    reference = {
        'discovery:main': {
            'Mop/s_total': (10000, -0.1, None, 'Mop/s')
        },
        'discovery:epyc-64': {
            'Mop/s_total': (25000, -0.1, None, 'Mop/s')
        },
        'discovery:gpu': {
            'Mop/s_total': (10000, -0.1, None, 'Mop/s')
        },
        'endeavour:shared': {
            'Mop/s_total': (10000, -0.1, None, 'Mop/s')
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'SUCCESSFUL', self.stdout)

    @performance_function('Mop/s', perf_key = 'Mop/s_total')
    def extract_perf(self):
        return sn.extractsingle(r'Mop/s total\s+=\s+(?P<mops_ret>\S+)', self.stdout, 'mops_ret', float)
