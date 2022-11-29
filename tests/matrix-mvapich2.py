import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matrix_MVAPICH2(rfm.RegressionTest):
    def __init__(self):
        self.descr = 'Matrix-vector multiplication example using gcc/11.3.0 and mvapich2/2.3.7 with pmi2'
        self.valid_systems = [
            'discovery:main',
            'discovery:epyc-64',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-gcc-11.3.0-mvapich2-2.3.7'
        ]
        self.sourcesdir = './src/matrix-mpi'
        self.sourcepath = 'matrix-vector-multiplication-mpi-openmp.c'
        self.executable_opts = [
            '4200',
            '10000'
        ]
        self.build_system = 'SingleSource'
        self.build_system.cflags = [
            '-fopenmp'
        ]
        self.num_tasks = 4
        self.num_tasks_per_node = 2
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.prerun_cmds = [
            'ulimit -s unlimited'
        ]
        self.variables = {
            'OMP_NUM_THREADS': '1',
            'SLURM_MPI_TYPE': 'pmi2',
            'SLURM_CPU_BIND': 'verbose',
            'MV2_USE_RDMA_CM': '0',
            'MV2_ENABLE_AFFINITY': '1'
        }
        self.sanity_patterns = sn.assert_found(r'time for single matrix vector multiplication', self.stdout)
        self.perf_patterns = {
            'elapsed time for multiplication': sn.extractsingle(r'multiplication\s(?P<time_ret>[0-9]+.[0-9]+)', self.stdout, 'time_ret', float)
        }
        self.reference = {
            '*': {
                'elapsed time for multiplication': (1.5, -0.25, 0.25, 'seconds')
            }
        }
