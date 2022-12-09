import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class QChem_B3LYP(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Q-Chem B3LYP functional'
        self.tags = {
            'daily'
        }
        self.valid_systems = [
            'discovery:main',
            'discovery:oneweek',
            'discovery:debug',
            'endeavour:shared'
        ]
        self.valid_prog_environs = [
            'PrgEnv-qchem'
        ]
        self.sourcesdir = './src/qchem-b3lyp'
        self.executable = 'qchem -nt $OMP_NUM_THREADS qchem-b3lyp.inp'
        self.num_tasks = 1
        self.num_cpus_per_task = 8
        self.time_limit = '5m'
        self.variables = {
            'OMP_NUM_THREADS': '8'
        }
        self.sanity_patterns = sn.assert_found(r'Thank you very much for using Q-Chem', self.stdout)
