# Q-Chem B3LYP-D3 functional parallel test
# Purpose of test
# - Test Q-Chem module access
# - Test Q-Chem license access
# - Test Q-Chem performance

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class QChem_B3LYP(rfm.RunOnlyRegressionTest):
    descr = "Q-Chem B3LYP-D3 functional"
    tags = {
        "maintenance",
        "singlenode"
    }
    valid_systems = [
        "discovery:allnodes",
        "endeavour:allnodes"
    ]
    valid_prog_environs = [
        "env-qchem"
    ]
    sourcesdir = "src/qchem-b3lyp"
    executable = "qchem -nt $OMP_NUM_THREADS qchem-b3lyp.inp"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "$SLURM_CPUS_PER_TASK"
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Thank you very much for using Q-Chem", self.stdout)
