# Endeavour configuration

site_configuration = {
    'general': [
        {
            'check_search_path': [
                'tests/'
            ],
            'check_search_recursive': True,
            'purge_environment': True,
            'report_file': '/project/hpcroot/reframe2/reports/endeavour-run-report-$(date --iso-8601=seconds).json',
        }
    ],
    'systems': [
        {
            'name': 'endeavour',
            'descr': 'Endeavour Cluster',
            'stagedir': '/project/hpcroot/reframe2/stage/endeavour-stage-$(date --iso-8601=seconds)',
            'outputdir': '/project/hpcroot/reframe2/output/endeavour-output-$(date --iso-8601=seconds)',
            'modules_system': 'lmod',
            'hostnames': [
                'endeavour.*'
            ],
            'partitions': [
                {
                    'name': 'shared',
                    'descr': 'Endeavour shared partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=shared'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-ior',
                        'PrgEnv-fio',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'cryoem',
                    'descr': 'Endeavour cryoem partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=cryoem'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-nvhpc-22.11',
                        'PrgEnv-nvhpc-23.11',
                        'PrgEnv-gcc-8.3.0-cuda-10.2.89',
                        'PrgEnv-gcc-11.3.0-cuda-11.6.2',
                        'PrgEnv-gcc-12.3.0-cuda-12.2.1',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'isi',
                    'descr': 'Endeavour isi partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=isi'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-nvhpc-22.11',
                        'PrgEnv-nvhpc-23.11',
                        'PrgEnv-gcc-8.3.0-cuda-10.2.89',
                        'PrgEnv-gcc-11.3.0-cuda-11.6.2',
                        'PrgEnv-gcc-12.3.0-cuda-12.2.1',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'priya',
                    'descr': 'Endeavour priya partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=priya'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-hpl',
                        'PrgEnv-hpcg',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'qcb',
                    'descr': 'Endeavour qcb partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=qcb'
                    ],
                    'max_jobs': 1000,
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-hpl',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'scec',
                    'descr': 'Endeavour scec partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=scec'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'PrgEnv-gcc-11.3.0',
            'modules': [
                'gcc/11.3.0'
            ],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'PrgEnv-gcc-12.3.0',
            'modules': [
                'gcc/12.3.0'
            ],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
            'modules': [
                'gcc/11.3.0',
                'openmpi/4.1.4'
            ],
            'cc': 'mpicc',
            'cxx': 'mpic++',
            'ftn': 'mpif90'
        },
        {
            'name': 'PrgEnv-gcc-11.3.0-mpich-4.0.2',
            'modules': [
                'gcc/11.3.0',
                'mpich/4.0.2'
            ],
            'cc': 'mpicc',
            'cxx': 'mpic++',
            'ftn': 'mpif90'
        },
        {
            'name': 'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
            'modules': [
                'gcc/11.3.0',
                'mvapich2/2.3.7'
            ],
            'cc': 'mpicc',
            'cxx': 'mpic++',
            'ftn': 'mpif90'
        },
        {
            'name': 'PrgEnv-hpl',
            'modules': [
                'gcc/11.3.0',
                'openblas/0.3.20',
                'openmpi/4.1.4',
                'hpl/2.3'
            ]
        },
        {
            'name': 'PrgEnv-hpcg',
            'modules': [
                'gcc/11.3.0',
                'openmpi/4.1.4',
                'hpcg/3.1'
            ]
        },
        {
            'name': 'PrgEnv-ior',
            'modules': [
                'gcc/11.3.0',
                'openmpi/4.1.4',
                'ucx/1.12.1',
                'ior/3.3.0'
            ]
        },
        {
            'name': 'PrgEnv-fio',
            'modules': [
            ]
        },
        {
            'name': 'PrgEnv-julia',
            'modules': [
                'julia/1.10.2'
            ]
        },
        {
            'name': 'PrgEnv-python3',
            'modules': [
                'gcc/11.3.0',
                'python/3.11.3'
            ]
        },
        {
            'name': 'PrgEnv-R',
            'modules': [
                'gcc/11.3.0',
                'openblas/0.3.20',
                'r/4.3.3'
            ]
        },
        {
            'name': 'PrgEnv-matlab',
            'modules': [
                'matlab/2022a'
            ]
        },
        {
            'name': 'PrgEnv-qchem',
            'modules': [
                'qchem/6.1.1'
            ]
        },
        {
            'name': 'PrgEnv-nvhpc-22.11',
            'modules': [
                'nvhpc/22.11'
            ]
        },
        {
            'name': 'PrgEnv-nvhpc-23.11',
            'modules': [
                'nvhpc/23.11'
            ]
        },
        {
             'name': 'PrgEnv-gcc-8.3.0-cuda-10.2.89',
             'modules': [
                 'gcc/8.3.0',
                 'cuda/10.2.89',
                 'openmpi/4.0.2'
             ]
        },
        {
             'name': 'PrgEnv-gcc-11.3.0-cuda-11.6.2',
             'modules': [
                 'gcc/11.3.0',
                 'cuda/11.6.2',
                 'openmpi/4.1.4'
             ]
        },
        {
             'name': 'PrgEnv-gcc-12.3.0-cuda-12.2.1',
             'modules': [
                 'gcc/12.3.0',
                 'cuda/12.2.1',
                 'openmpi/4.1.5'
             ]
        },
        {
             'name': 'PrgEnv-singularity',
             'modules': [
             ]
        },
        {
            'name': 'PrgEnv-curl',
            'modules': [
                'gcc/11.3.0',
                'curl/7.83.0'
            ]
        }
    ],
    'logging': [
        {
            'handlers': [
                {
                    'type': 'file',
                    'level': 'debug',
                    'name': './logs/reframe-endeavour.log',
                    'timestamp': '%FT%T',
                    'format': '[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s',
                    'append': True
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    'level': 'info',
                    'basedir': './perflogs',
                    'prefix': '%(check_system)s/%(check_partition)s',
                    'format': (
                        '%(check_job_completion_time)s,%(version)s,'
                        '%(check_display_name)s,%(check_system)s,'
                        '%(check_partition)s,%(check_environ)s,'
                        '%(check_jobid)s,%(check_result)s,%(check_perfvalues)s'
                    ),
                    'format_perfvars': (
                        '%(check_perf_value)s,%(check_perf_unit)s,'
                        '%(check_perf_ref)s,%(check_perf_lower_thres)s,'
                        '%(check_perf_upper_thres)s,'
                    ),
                    'datefmt': '%FT%T',
                    'append': True
                }
            ]
        }
    ]
}
