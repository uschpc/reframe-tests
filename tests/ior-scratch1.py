import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class IOR_scratch1(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'IOR benchmark for /scratch1 file system'
        self.tags = {
            'daily'
        }
        self.valid_systems = [
            'discovery:epyc-64',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-ior'
        ]
        self.sourcesdir = None
        self.executable = 'ior -vvv -t 4m -b 64m -s 16 -F -C -e -o /scratch1/$USER/reframe.tmp'
        self.num_tasks = 16
        self.num_tasks_per_node = 4
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'Finished', self.stdout)
        self.perf_patterns = {
            'max write speed': sn.extractsingle(r'Max Write:\s+(?P<W_ret>\S+)', self.stdout, 'W_ret', float),
            'max read speed': sn.extractsingle(r'Max Read:\s+(?P<R_ret>\S+)', self.stdout, 'R_ret', float)
        }
        self.reference = {
            '*': {
                'max write speed': (3000.00, -0.25, None, 'MiB/sec'),
                'max read speed': (15000.00, -0.25, None, 'MiB/sec')
            }
        }
