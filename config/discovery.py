# Discovery configuration

site_configuration = {
    'general': [
        {
            'check_search_path': [
                'tests/'
            ],
            'check_search_recursive': True,
            'purge_environment': True,
            'report_file': '/project/hpcroot/reframe2/reports/discovery-run-report-$(date --iso-8601=seconds).json',
        }
    ],
    'systems': [
        {
            'name': 'discovery',
            'descr': 'Discovery Cluster',
            'stagedir': '/project/hpcroot/reframe2/stage/discovery-stage-$(date --iso-8601=seconds)',
            'outputdir': '/project/hpcroot/reframe2/output/discovery-output-$(date --iso-8601=seconds)',
            'modules_system': 'lmod',
            'hostnames': [
                'discovery.*'
            ],
            'partitions': [
                {
                    'name': 'main',
                    'descr': 'Discovery main partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                        '--account=hpcroot',
                        '--partition=main'
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
                        'PrgEnv-pgi',
                        'PrgEnv-gcc-8.3.0-cuda-10.2.89',
                        'PrgEnv-gcc-11.3.0-cuda-11.6.2',
                        'PrgEnv-intel-19.0.4-cuda-10.2.89',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'epyc-64',
                    'descr': 'Discovery epyc-64 partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                         '--account=hpcroot',
                         '--partition=epyc-64'
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
                    'name': 'gpu',
                    'descr': 'Discovery gpu partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                         '--account=hpcroot',
                         '--partition=gpu'
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
                        'PrgEnv-nvhpc',
                        'PrgEnv-pgi',
                        'PrgEnv-gcc-8.3.0-cuda-10.2.89',
                        'PrgEnv-gcc-11.3.0-cuda-11.6.2',
                        'PrgEnv-intel-19.0.4-cuda-10.2.89',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'largemem',
                    'descr': 'Discovery largemem partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                         '--account=hpcroot',
                         '--partition=largemem'
                    ],
                    'environs': [
                        'PrgEnv-gcc-11.3.0',
                        'PrgEnv-gcc-12.3.0',
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
                    'name': 'debug',
                    'descr': 'Discovery debug partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                         '--account=hpcroot',
                         '--partition=debug'
                    ],
                    'environs': [
                        'PrgEnv-julia',
                        'PrgEnv-nvhpc',
                        'PrgEnv-python3',
                        'PrgEnv-singularity',
                        'PrgEnv-curl'
                    ]
                },
                {
                    'name': 'oneweek',
                    'descr': 'Discovery oneweek partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': [
                         '--account=hpcroot',
                         '--partition=oneweek'
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
                'openmpi/4.1.4',
                'ucx/1.12.1'
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
                'julia/1.9.3'
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
                'r/4.3.1'
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
                'qchem/6.1.0'
            ]
        },
        {
            'name': 'PrgEnv-nvhpc',
            'modules': [
                'nvhpc/22.11'
            ]
        },
        {
            'name': 'PrgEnv-pgi',
            'modules': [
                'gcc/8.3.0',
                'pgi-nvhpc'
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
             'name': 'PrgEnv-intel-19.0.4-cuda-10.2.89',
             'modules': [
                 'intel/19.0.4',
                 'cuda/10.2.89'
             ],
             'cc': 'icc',
             'cxx': 'icpc',
             'ftn': 'ifort'
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
                    'name': './logs/reframe-discovery.log',
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
