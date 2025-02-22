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
            "descr": "Discovery cluster",
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio",
                        "env-ior"
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio",
                        "env-ior"
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio",
                        "env-ior"
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio"
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio"
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
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio"
                    ]
                }
            ]
        }
    ],
    "environments": [
        {
             "name": "env-apptainer",
             "modules": [
                 "apptainer/1.3.3"
             ]
        },
        {
            "name": "env-gcc-13.3.0",
            "modules": [
                "gcc/13.3.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-cuda-12.6.3",
            "modules": [
                "gcc/13.3.0",
                "cuda/12.6.3"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-openmpi-5.0.5",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90",
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmix_v5"]
            ]
        },
        {
            "name": "env-gcc-13.3.0-mpich-4.2.2",
            "modules": [
                "gcc/13.3.0",
                "mpich/4.2.2"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90",
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmi2"]
            ]
        },
        {
            "name": "env-hpcg",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "hpcg/3.1"
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.11.2"
            ]
        },
        {
            "name": "env-python",
            "modules": [
                "gcc/13.3.0",
                "python/3.11.9"
            ]
        },
        {
            "name": "env-r",
            "modules": [
                "gcc/13.3.0",
                "r/4.4.2"
            ]
        },
        {
            "name": "env-matlab",
            "modules": [
                "matlab/2024a"
            ]
        },
        {
            "name": "env-qchem",
            "modules": [
                "qchem/6.2.0"
            ]
        },
        {
            "name": "env-curl",
            "modules": [
                "gcc/13.3.0",
                "curl/8.8.0"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
                "gcc/13.3.0",
                "fio/3.37",
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "ior/3.3.0"
            ]
        },
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
