# NAS Parallel Benchmarks MPI EP (embarrassingly parallel) benchmark test
# Purpose of test
# - Test MPI module access
# - Test building Fortran/MPI program
# - Test running Fortran/MPI program
# - Test collective performance of Discovery epyc-64 partition
#   targeting maximum flop/s

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class npb_mpi_ep_discovery_epyc(rfm.RunOnlyRegressionTest):
    descr = "NPB MPI EP benchmark for Discovery epyc-64 partition"
    tags = {
        "multinode",
        "performance"
    }
    valid_systems = [
        "discovery:epyc-64"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-openmpi-5.0.5"
    ]
    sourcesdir = "src/npb-mpi"
    executable = "ep.E.x"
    num_tasks = 4992
    num_tasks_per_node = 64
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "bash make-npb-mpi.sh ep E"
    ]
    reference = {
        "*": {
            "Mop/s_total": (200000, -0.1, None, "Mop/s")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
