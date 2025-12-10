# stress-ng memory test
# Purpose of test
# - Test Apptainer module access
# - Test Apptainer exec
# - Stress test memory
# Notes
# - https://github.com/ColinIanKing/stress-ng

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class stress_ng_mem(rfm.RunOnlyRegressionTest):
    descr = "Stress test memory with stress-ng"
    tags = {
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "pathfinder:allnodes",
        "laguna:allnodes"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = None
    executable = "sleep 1s"
    time_limit = "5m"
    prerun_cmds = [
        "apptainer exec /apps/reframe/resources/containers/stress-ng.sif stress-ng --vm $SLURM_CPUS_ON_NODE --vm-bytes 95% --timeout 2m"
    ]

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--exclusive",
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"failed: 0", self.stdout)
