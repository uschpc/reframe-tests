import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_BT_MZ_MPICH(rfm.RunOnlyRegressionTest):
    descr = 'NPB BT-MZ MPI+OpenMP benchmark using gcc/11.3.0 and mpich/4.0.2 with pmi2'
    valid_systems = [
        'discovery:main',
        'discovery:epyc-64',
        'discovery:gpu',
        'discovery:debug',
        'discovery:oneweek',
        'endeavour:shared',
        'endeavour:cryoem',
        'endeavour:isi',
        'endeavour:priya',
        'endeavour:qcb',
        'endeavour:scec'
    ]
    valid_prog_environs = [
        'PrgEnv-gcc-11.3.0-mpich-4.0.2'
    ]
    sourcesdir = None
    executable = '/project/hpcroot/reframe2/resources/NPB/gcc-11.3.0/NPB3.4.2-MZ/NPB3.4-MZ-MPI-mpich-4.0.2/bin/bt-mz.A.x'
    num_tasks = 4
    num_tasks_per_node = 2
    num_cpus_per_task = 2
    time_limit = '5m'
    prerun_cmds = [
        'ulimit -s unlimited'
    ]
    env_vars = {
        'OMP_NUM_THREADS': '2',
        'SLURM_MPI_TYPE': 'pmi2',
        'SLURM_CPU_BIND': 'verbose'
    }
    reference = {
        'discovery:main': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'discovery:epyc-64': {
            'Mop/s_total': (45000, -0.1, None, 'Mop/s')
        },
        'discovery:gpu': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'discovery:debug': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'discovery:oneweek': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'endeavour:shared': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'endeavour:cryoem': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'endeavour:isi': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'endeavour:priya': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        },
        'endeavour:qcb': {
            'Mop/s_total': (22000, -0.1, None, 'Mop/s')
        },
        'endeavour:scec': {
            'Mop/s_total': (26000, -0.1, None, 'Mop/s')
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'SUCCESSFUL', self.stdout)

    @performance_function('Mop/s', perf_key = 'Mop/s_total')
    def extract_perf(self):
        return sn.extractsingle(r'Mop/s total\s+=\s+(?P<mops_ret>\S+)', self.stdout, 'mops_ret', float)
