# HTCondor test
# Purpose of test
# - Test if HTCondor is available

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class htcondor_avail(rfm.RunOnlyRegressionTest):
    descr = "HTCondor availability"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:htcondor",
        "laguna:htcondor"
    ]
    valid_prog_environs = [
        "env-none"
    ]
    sourcesdir = None
    executable = "condor_q"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Total for all users", self.stdout)
