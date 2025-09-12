# Git clone test
# Purpose of test
# - Test git module access
# - Test public internet access via git clone of remote repo
# - Test git clone on /home file system

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class git_clone_home(rfm.RunOnlyRegressionTest):
    descr = "Git clone on /home file system"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "pathfinder:allnodes"
    ]
    valid_prog_environs = [
        "env-git"
    ]
    sourcesdir = "src/git-clone"
    executable = "bash git-clone.sh home"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_not_found(r"fatal", self.stderr)
