import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Singularity_GPU_Hello(rfm.RunOnlyRegressionTest):
    descr = 'Singularity GPU access'
    valid_systems = [
        'discovery:main',
        'discovery:gpu',
        'discovery:debug',
        'endeavour:cryoem',
        'endeavour:isi'
    ]
    valid_prog_environs = [
        'PrgEnv-singularity'
    ]
    sourcesdir = None
    executable = 'singularity exec --nv /spack/singularity/ood/desktop/centos7-xfce-desktop-ood3.sif echo "Hello world from $(nvidia-smi -L)"'
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
        return sn.assert_found(r'UUID', self.stdout)
