import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class File_Download(rfm.RunOnlyRegressionTest):
    descr = 'File download'
    tags = {
        'daily'
    }
    valid_systems = [
        'discovery:main',
        'discovery:epyc-64',
        'discovery:gpu',
        'discovery:largemem',
        'discovery:debug',
        'discovery:oneweek',
        'endeavour:shared',
        'endeavour:isi'
    ]
    valid_prog_environs = [
        'PrgEnv-curl'
    ]
    sourcesdir = None
    executable = 'curl -LO https://carc.usc.edu/index.html |& cat'
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = '5m'

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'100', self.stdout)
