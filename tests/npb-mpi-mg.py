# NAS Parallel Benchmarks MPI MG (multigrid) benchmark test
# Purpose of test
# - Test MPI module access
# - Test building Fortran/MPI program
# - Test running Fortran/MPI program
# - Test collective node performance for differential equations solver
#   using multigrid method
# Notes
# - Requires a power-of-two number of CPU cores

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class NPB_MPI_MG(rfm.RunOnlyRegressionTest):
    descr = "NPB MPI MG benchmark"
    tags = {
        "maintenance",
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:epyc-7513",
        "endeavour:allnodes",
        "pathfinder:allnodes",
        "laguna:allnodes"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-openmpi-5.0.5",
        "env-gcc-13.3.0-mpich-4.2.2"
    ]
    sourcesdir = "src/npb-mpi"
    executable = "mg.D.x"
    num_tasks = 32
    num_tasks_per_node = 16
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-mpi.sh mg D"
    ]
    reference = {
        "discovery:epyc-7513": {
            "Mop/s_total": (50000, -0.1, None, "Mop/s")
        },
        "*": {
            "Mop/s_total": (40000, -0.1, None, "Mop/s")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
