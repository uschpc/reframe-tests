import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Matrix_MVAPICH2(rfm.RegressionTest):
    descr = 'Matrix-vector multiplication example using gcc/11.3.0 and mvapich2/2.3.7 with pmi2'
    valid_systems = [
        'discovery:main',
        'discovery:epyc-64',
        'discovery:gpu',
        'endeavour:shared'
    ]
    valid_prog_environs = [
        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7'
    ]
    sourcesdir = './src/matrix-mpi'
    sourcepath = 'matrix-vector-multiplication-mpi-openmp.c'
    executable_opts = [
        '4200',
        '10000'
    ]
    build_system = 'SingleSource'
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
        '*': {
            'elapsed_time': (1.5, None, 0.25, 'seconds')
        }
    }

    @run_before('compile')
    def set_compiler_flags(self):
        self.build_system.cflags = [
            '-fopenmp'
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'time for single matrix vector multiplication', self.stdout)

    @performance_function('seconds', perf_key = 'elapsed_time')
    def extract_perf(self):
        return sn.extractsingle(r'multiplication\s(?P<time_ret>[0-9]+.[0-9]+)', self.stdout, 'time_ret', float)
