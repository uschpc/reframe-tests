# NAS Parallel Benchmarks MPI IS (integer sort) benchmark test
# Purpose of test
# - Test MPI module access
# - Test building C/MPI program
# - Test running C/MPI program
# - Test collective node performance for integer sort algorithm

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_mpi_is(rfm.RunOnlyRegressionTest):
    descr = "NPB MPI IS benchmark"
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
    executable = "is.D.x"
    num_tasks = 32
    num_tasks_per_node = 16
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-mpi.sh is D"
    ]
    reference = {
        "discovery:epyc-7513": {
            "Mop/s_total": (1500, -0.1, None, "Mop/s")
        },
        "*": {
            "Mop/s_total": (1300, -0.1, None, "Mop/s")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
