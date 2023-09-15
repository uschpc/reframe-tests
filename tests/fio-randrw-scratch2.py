import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Fio_randrw_scratch2(rfm.RunOnlyRegressionTest):
    descr = 'Fio random read/write benchmark for /scratch2 file system'
    tags = {
        'daily'
    }
    valid_systems = [
        'discovery:epyc-64',
        'endeavour:shared',
        'endeavour:cryoem',
        'endeavour:isi',
        'endeavour:priya',
        'endeavour:qcb',
        'endeavour:scec'
    ]
    valid_prog_environs = [
        'PrgEnv-fio'
    ]
    sourcesdir = None
    sourcesdir = './src/fio-randrw'
    executable = 'bash fio-randrw.sh /scratch2/$USER'
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = '10m'
    reference = {
        '*': {
            'avg_write_speed': (15.00, -0.25, None, 'MiB/sec'),
            'avg_read_speed': (15.00, -0.25, None, 'MiB/sec')
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'all jobs', self.stdout)

    @performance_function('MiB/sec', perf_key = 'avg_write_speed')
    def extract_perf_write(self):
        return sn.extractsingle(r'WRITE:\sbw=(?P<W_ret>\d+.\d+)', self.stdout, 'W_ret', float)

    @performance_function('MiB/sec', perf_key = 'avg_read_speed')
    def extract_perf_read(self):
        return sn.extractsingle(r'READ:\sbw=(?P<R_ret>\d+.\d+)', self.stdout, 'R_ret', float)
