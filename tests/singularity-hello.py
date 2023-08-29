import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Singularity_Hello(rfm.RunOnlyRegressionTest):
    descr = 'Singularity hello world'
    valid_systems = [
        'discovery:main',
        'discovery:epyc-64',
        'discovery:gpu',
        'discovery:largemem',
        'discovery:debug',
        'discovery:oneweek',
        'endeavour:shared'
    ]
    valid_prog_environs = [
        'PrgEnv-singularity'
    ]
    sourcesdir = None
    executable = 'singularity exec /spack/singularity/ood/centos7-xfce-oodv3.sif echo \"Hello world\"'
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = '5m'

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'Hello world', self.stdout)
