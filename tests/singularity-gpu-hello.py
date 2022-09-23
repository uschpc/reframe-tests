import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class SingularityGPUHello(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Singularity GPU access'
        self.tags = {
            'daily'
        }
        self.valid_systems = [
            'discovery:gpu'
        ]
        self.valid_prog_environs = [
            'PrgEnv-singularity'
        ]
        self.sourcesdir = None
        self.executable = 'singularity exec --nv /spack/singularity/ood/centos7-xfce.sif nvidia-smi'
        self.num_tasks = 1
        self.num_cpus_per_task = 1
        self.time_limit = '5m'
        self.sanity_patterns = sn.assert_found(r'NVIDIA-SMI', self.stdout)

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--gres=gpu:p100:1',
            '--gres-flags=enforce-binding'
        ]
