# Slurm salloc test
# Purpose of test
# - Test salloc on each login node

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Salloc_Hello(rfm.RunOnlyRegressionTest):
    descr = "Run salloc and exit"
    tags = {
        "local",
        "maintenance"
    }
    valid_systems = [
        "discovery:login",
        "endeavour:login",
        "pathfinder:login",
        "laguna:login"
    ]
    valid_prog_environs = [
        "env-none"
    ]
    sourcesdir = "src/salloc"
    executable = "bash salloc.sh"

    @sanity_function
    def assert_sanity(self):
        matches = sn.findall(r"Relinquishing job allocation", self.stderr)
        nmatches = sn.len(matches)
        if self.current_system.name in ["discovery", "endeavour"]:
            return sn.assert_eq(nmatches, 2)
        else:
            return sn.assert_eq(nmatches, 1)
