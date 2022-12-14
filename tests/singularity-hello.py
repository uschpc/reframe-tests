import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Singularity_Hello(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Singularity hello world'
        self.valid_systems = [
            'discovery:main',
            'discovery:oneweek',
            'discovery:debug',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-singularity'
        ]
        self.sourcesdir = None
        self.executable = 'singularity exec /spack/singularity/ood/centos7-xfce.sif echo \"Hello world\"'
        self.num_tasks = 1
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'Hello world', self.stdout)
