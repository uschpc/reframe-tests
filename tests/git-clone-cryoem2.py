# Git clone test
# Purpose of test
# - Test git module access
# - Test public internet access via git clone of remote repo
# - Test git clone on /cryoem2 file system

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Git_clone_cryoem2(rfm.RunOnlyRegressionTest):
    descr = "Git clone on /cryoem2 file system"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-git"
    ]
    sourcesdir = "src/git-clone"
    executable = "bash git-clone.sh cryoem2"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_not_found(r"fatal", self.stderr)
