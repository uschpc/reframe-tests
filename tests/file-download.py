import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class File_Download(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'File download'
        self.tags = {
            'daily'
        }
        self.valid_systems = [
            'discovery:main',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-aria2'
        ]
        self.sourcesdir = None
        self.executable = 'aria2c https://github.com/reframe-hpc/reframe/archive/refs/tags/v3.12.0.tar.gz'
        self.num_tasks = 1
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(
            r'download completed', self.stdout
        )
