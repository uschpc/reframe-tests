# NAS Parallel Benchmarks MPI IS (integer sort) benchmark test
# Purpose of test
# - Test MPI module access
# - Test building C/MPI program
# - Test running C/MPI program
# - Test collective node performance for integer sort algorithm
# Notes
# - https://www.nas.nasa.gov/software/npb.html

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
        "endeavour:epyc-7513",
        "pathfinder:xeon-2640v3",
        "laguna:epyc-9554"
    ]
    valid_prog_environs = [
        "env-gcc-14.3.0-openmpi-5.0.8",
        "env-gcc-14.3.0-mpich-4.3.1",
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
            "Mop/s_total": (2555, -0.2, 0.2, "Mop/s")
        },
        "endeavour:epyc-7513": {
            "Mop/s_total": (2555, -0.2, 0.2, "Mop/s")
        },
        "pathfinder:xeon-2640v3": {
            "Mop/s_total": (930, -0.2, 0.2, "Mop/s")
        },
        "laguna:epyc-9554": {
            "Mop/s_total": (3650, -0.2, 0.2, "Mop/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Verification\s+=\s+SUCCESSFUL", self.stdout)

    @performance_function("Mop/s", perf_key = "Mop/s_total")
    def extract_perf(self):
        return sn.extractsingle(r"Mop/s total\s+=\s+(?P<mops_ret>\S+)", self.stdout, "mops_ret", float)
