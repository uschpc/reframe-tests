# Discovery configuration

site_configuration = {
    "general": [
        {
            "check_search_path": [
                "tests/"
            ],
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/project/hpcroot/rfm/reports/discovery-run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "discovery",
            "descr": "Discovery Cluster",
            "stagedir": "/project/hpcroot/rfm/stage/discovery-stage-$(date --iso-8601=seconds)",
            "outputdir": "/project/hpcroot/rfm/output/discovery-output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "discovery.*"
            ],
            "partitions": [
                {
                    "name": "main",
                    "descr": "Discovery main partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=main"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-gcc-11.3.0-openmpi-4.1.4",
                        "env-gcc-11.3.0-mpich-4.0.2",
                        "env-gcc-11.3.0-mvapich2-2.3.7",
                        "env-hpl",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-gcc-8.3.0-cuda-10.2.89",
                        "env-gcc-11.3.0-cuda-11.6.2",
                        "env-singularity",
                        "env-curl"
                    ]
                },
                {
                    "name": "epyc-64",
                    "descr": "Discovery epyc-64 partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=epyc-64"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-gcc-11.3.0-openmpi-4.1.4",
                        "env-gcc-11.3.0-mpich-4.0.2",
                        "env-gcc-11.3.0-mvapich2-2.3.7",
                        "env-hpl",
                        "env-hpcg",
                        "env-ior",
                        "env-fio",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-singularity",
                        "env-curl"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Discovery gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=gpu"
                    ],
                    "max_jobs": 100,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-gcc-11.3.0-openmpi-4.1.4",
                        "env-gcc-11.3.0-mpich-4.0.2",
                        "env-gcc-11.3.0-mvapich2-2.3.7",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-nvhpc-22.11",
                        "env-nvhpc-23.11",
                        "env-gcc-8.3.0-cuda-10.2.89",
                        "env-gcc-11.3.0-cuda-11.6.2",
                        "env-gcc-12.3.0-cuda-12.2.1",
                        "env-singularity",
                        "env-curl"
                    ]
                },
                {
                    "name": "largemem",
                    "descr": "Discovery largemem partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=largemem"
                    ],
                    "max_jobs": 10,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-singularity",
                        "env-curl"
                    ]
                },
                {
                    "name": "debug",
                    "descr": "Discovery debug partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=debug"
                    ],
                    "max_jobs": 5,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-gcc-11.3.0-openmpi-4.1.4",
                        "env-gcc-11.3.0-mpich-4.0.2",
                        "env-gcc-11.3.0-mvapich2-2.3.7",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-nvhpc-22.11",
                        "env-nvhpc-23.11",
                        "env-gcc-11.3.0-cuda-11.6.2",
                        "env-gcc-12.3.0-cuda-12.2.1",
                        "env-singularity",
                        "env-curl"
                    ]
                },
                {
                    "name": "oneweek",
                    "descr": "Discovery oneweek partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=oneweek"
                    ],
                    "max_jobs": 50,
                    "environs": [
                        "env-gcc-11.3.0",
                        "env-gcc-12.3.0",
                        "env-gcc-11.3.0-openmpi-4.1.4",
                        "env-gcc-11.3.0-mpich-4.0.2",
                        "env-gcc-11.3.0-mvapich2-2.3.7",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-singularity",
                        "env-curl"
                    ]
                }
            ]
        }
    ],
    "environments": [
        {
            "name": "env-gcc-11.3.0",
            "modules": [
                "gcc/11.3.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-12.3.0",
            "modules": [
                "gcc/12.3.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-11.3.0-openmpi-4.1.4",
            "modules": [
                "gcc/11.3.0",
                "openmpi/4.1.4",
                "ucx/1.12.1"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-11.3.0-mpich-4.0.2",
            "modules": [
                "gcc/11.3.0",
                "mpich/4.0.2"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-11.3.0-mvapich2-2.3.7",
            "modules": [
                "gcc/11.3.0",
                "mvapich2/2.3.7"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-hpl",
            "modules": [
                "gcc/11.3.0",
                "openblas/0.3.20",
                "openmpi/4.1.4",
                "hpl/2.3"
            ]
        },
        {
            "name": "env-hpcg",
            "modules": [
                "gcc/11.3.0",
                "openmpi/4.1.4",
                "hpcg/3.1"
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "gcc/11.3.0",
                "openmpi/4.1.4",
                "ucx/1.12.1",
                "ior/3.3.0"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.10.3"
            ]
        },
        {
            "name": "env-python",
            "modules": [
                "gcc/11.3.0",
                "python/3.11.3"
            ]
        },
        {
            "name": "env-r",
            "modules": [
                "gcc/11.3.0",
                "openblas/0.3.20",
                "r/4.4.1"
            ]
        },
        {
            "name": "env-matlab",
            "modules": [
                "matlab/2022a"
            ]
        },
        {
            "name": "env-qchem",
            "modules": [
                "qchem/6.1.1"
            ]
        },
        {
            "name": "env-nvhpc-22.11",
            "modules": [
                "nvhpc/22.11"
            ]
        },
        {
            "name": "env-nvhpc-23.11",
            "modules": [
                "nvhpc/23.11"
            ]
        },
        {
             "name": "env-gcc-8.3.0-cuda-10.2.89",
             "modules": [
                 "gcc/8.3.0",
                 "cuda/10.2.89",
                 "openmpi/4.0.2"
             ]
        },
        {
             "name": "env-gcc-11.3.0-cuda-11.6.2",
             "modules": [
                 "gcc/11.3.0",
                 "cuda/11.6.2",
                 "openmpi/4.1.4"
             ]
        },
        {
             "name": "env-gcc-12.3.0-cuda-12.2.1",
             "modules": [
                 "gcc/12.3.0",
                 "cuda/12.2.1",
                 "openmpi/4.1.5"
             ]
        },
        {
             "name": "env-singularity",
             "modules": [
             ]
        },
        {
            "name": "env-curl",
            "modules": [
                "gcc/11.3.0",
                "curl/7.83.0"
            ]
        }
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "./logs/reframe-discovery.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "./perflogs",
                    "prefix": "%(check_system)s/%(check_partition)s",
                    "format": (
                        "%(check_job_completion_time)s,%(version)s,"
                        "%(check_display_name)s,%(check_system)s,"
                        "%(check_partition)s,%(check_environ)s,"
                        "%(check_jobid)s,%(check_result)s,%(check_perfvalues)s"
                    ),
                    "format_perfvars": (
                        "%(check_perf_value)s,%(check_perf_unit)s,"
                        "%(check_perf_ref)s,%(check_perf_lower_thres)s,"
                        "%(check_perf_upper_thres)s,"
                    ),
                    "datefmt": "%FT%T",
                    "append": True
                }
            ]
        }
    ]
}
