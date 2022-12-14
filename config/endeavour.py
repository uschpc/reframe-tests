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
                        'PrgEnv-gcc-11.3.0-openmpi-4.1.4',
                        'PrgEnv-gcc-11.3.0-mpich-4.0.2',
                        'PrgEnv-gcc-11.3.0-mvapich2-2.3.7',
                        'PrgEnv-ior',
                        'PrgEnv-julia',
                        'PrgEnv-python3',
                        'PrgEnv-R',
                        'PrgEnv-aria2',
                        'PrgEnv-matlab',
                        'PrgEnv-qchem',
                        'PrgEnv-singularity'
                    ]
                }
            ]
        }
    ],
   'schedulers': [
        { 'name': 'slurm',
          'use_nodes_option': False
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
            'name': 'PrgEnv-ior',
            'modules': [
                'gcc/11.3.0',
                'openmpi/4.1.4',
                'ucx/1.12.1',
                'ior/3.3.0'
            ]
        },
        {
            'name': 'PrgEnv-julia',
            'modules': [
                'julia/1.8.3'
            ]
        },
        {
            'name': 'PrgEnv-python3',
            'modules': [
                'gcc/11.3.0',
                'python/3.9.12'
            ]
        },
        {
            'name': 'PrgEnv-R',
            'modules': [
                'gcc/11.3.0',
                'openblas/0.3.20',
                'r/4.2.1'
            ]
        },
        {
            'name': 'PrgEnv-aria2',
            'modules': [
                'gcc/11.3.0',
                'aria2/1.36.0'
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
                'qchem/6.0.1'
            ]
        },
        {
             'name': 'PrgEnv-singularity',
             'modules': [
             ]
        }
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'stream',
                    'level': 'info',
                    'name': 'stdout',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'level': 'info',
                    'name': './logs/reframe-endeavour.out',
                    'timestamp': '%FT%T',
                    'format': '%(message)s',
                    'append': True
                },
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
                        '%(check_job_completion_time)s|'
                        '%(check_info)s|'
                        'jobid=%(check_jobid)s|'
                        'nodelist=%(check_job_nodelist)s|'
                        '%(check_perf_var)s=%(check_perf_value)s|'
                        'ref=%(check_perf_ref)s '
                        '(l=%(check_perf_lower_thres)s, '
                        'u=%(check_perf_upper_thres)s)|'
                        '%(check_perf_unit)s'
                    ),
                    'datefmt': '%FT%T',
                    'append': True
                }
            ]
        }
    ]
}
