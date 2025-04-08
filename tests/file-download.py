# File download test
# Purpose of test
# - Test curl module access
# - Test public internet access via download

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class File_Download(rfm.RunOnlyRegressionTest):
    descr = "File download"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes",
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-curl"
    ]
    sourcesdir = None
    executable = "curl -L https://carc.usc.edu/index.html"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"USC Center for Advanced Research Computing", self.stdout)
