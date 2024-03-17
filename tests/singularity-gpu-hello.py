import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Singularity_GPU_Hello(rfm.RunOnlyRegressionTest):
    descr = 'Singularity GPU access'
    valid_systems = [
        'discovery:gpu',
        'discovery:debug',
        'endeavour:cryoem',
        'endeavour:isi'
    ]
    valid_prog_environs = [
        'PrgEnv-singularity'
    ]
    sourcesdir = None
    executable = 'singularity exec --nv /spack/singularity/ood/centos7-xfce-oodv3.sif nvidia-smi'
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = '5m'

    @run_before('run')
    def set_job_options(self):
        self.job.options += [
            '--gpus-per-task=1'
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'NVIDIA-SMI', self.stdout)
