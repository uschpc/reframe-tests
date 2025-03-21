import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_MZ_MPI_OMP_LU(rfm.RunOnlyRegressionTest):
    descr = "NPB MZ MPI/OMP LU benchmark"
    tags = {
        "maintenance"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-openmpi-5.0.5",
        "env-gcc-13.3.0-mpich-4.2.2"
    ]
    sourcesdir = "src/npb-mz-mpi-omp-lu"
    executable = "lu-mz.D.x"
    num_tasks = 8
    num_tasks_per_node = 2
    num_cpus_per_task = 32
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_PER_TASK"
    }
    prerun_cmds = [
        "bash make-npb-mz-mpi-omp-lu.sh"
    ]
    reference = {
        "*": {
            "Mop/s_total": (600000, -0.1, None, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--constraint=epyc-7513"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
