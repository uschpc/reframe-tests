# PMI test
# Purpose of test
# - Verify available PMI options for Slurm

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class pmi(rfm.RunOnlyRegressionTest):
    descr = "PMI verification"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "pathfinder:allnodes",
        "laguna:allnodes"
    ]
    valid_prog_environs = [
        "env-none"
    ]
    sourcesdir = None
    executable = "srun --mpi=list"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        pmi = sn.assert_found(r"pmi2", self.stdout)
        pmix_v2 = sn.assert_found(r"pmix_v2", self.stdout)
        pmix_v3 = sn.assert_found(r"pmix_v3", self.stdout)
        pmix_v4 = sn.assert_found(r"pmix_v4", self.stdout)
        pmix_v5 = sn.assert_found(r"pmix_v5", self.stdout)
        res = all([pmi, pmix_v2, pmix_v3, pmix_v4, pmix_v5])
        return sn.assert_true(res)
