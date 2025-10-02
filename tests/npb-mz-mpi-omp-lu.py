# NAS Parallel Benchmarks Multi-Zone LU benchmark test
# Purpose of test
# - Test MPI module access
# - Test building hybrid Fortran/MPI/OpenMP program
# - Test running hybrid Fortran/MPI/OpenMP program
# - Test collective node performance for flow solver
#   using Lower-Upper Symmetric-Gauss-Seidel method

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_mz_mpi_omp_lu(rfm.RunOnlyRegressionTest):
    descr = "NPB MZ MPI/OMP LU benchmark"
    tags = {
        "maintenance",
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:epyc-7513",
        "endeavour:epyc-7513",
        "laguna:epyc-9354"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-openmpi-5.0.5",
        "env-gcc-13.3.0-mpich-4.2.2"
    ]
    sourcesdir = "src/npb-mz-mpi-omp"
    executable = "lu-mz.D.x"
    num_tasks = 8
    num_tasks_per_node = 2
    num_cpus_per_task = 32
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_PER_TASK"
    }
    prerun_cmds = [
        "bash make-npb-mz-mpi-omp.sh lu-mz D"
    ]
    reference = {
        "discovery:epyc-7513": {
            "Mop/s_total": (600000, -0.1, 0.1, "Mop/s")
        },
        "endeavour:epyc-7513": {
            "Mop/s_total": (622000, -0.1, 0.1, "Mop/s")
        },
        "laguna:epyc-9354": {
            "Mop/s_total": (1065811, -0.1, 0.1, "Mop/s")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
