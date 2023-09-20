import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class QChem_B3LYP(rfm.RunOnlyRegressionTest):
    descr = 'Q-Chem B3LYP functional'
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
        'endeavour:cryoem',
        'endeavour:isi',
        'endeavour:priya',
        'endeavour:qcb',
        'endeavour:scec'
    ]
    valid_prog_environs = [
        'PrgEnv-qchem'
    ]
    sourcesdir = './src/qchem-b3lyp'
    executable = 'qchem -nt $OMP_NUM_THREADS qchem-b3lyp.inp'
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = '5m'
    env_vars = {
        'OMP_NUM_THREADS': '8'
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'Thank you very much for using Q-Chem', self.stdout)
