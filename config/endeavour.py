# Endeavour configuration

site_configuration = {
    "general": [
        {
            "check_search_path": [
                "tests/"
            ],
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/project/hpcroot/rfm/reports/endeavour-run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "endeavour",
            "descr": "Endeavour cluster",
            "stagedir": "/project/hpcroot/rfm/stage/endeavour-stage-$(date --iso-8601=seconds)",
            "outputdir": "/project/hpcroot/rfm/output/endeavour-output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "endeavour.*"
            ],
            "partitions": [
                {
                    "name": "shared",
                    "descr": "Endeavour shared partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=shared"
                    ],
                    "max_jobs": 5000,
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
                        "env-fio",
                        "env-ior"
                    ]
                },
                {
                    "name": "cryoem",
                    "descr": "Endeavour cryoem partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=cryoem"
                    ],
                    "max_jobs": 5000,
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
                        "env-nvhpc-24.5"
                    ]
                },
                {
                    "name": "isi",
                    "descr": "Endeavour isi partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=isi"
                    ],
                    "max_jobs": 5000,
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
                        "env-nvhpc-24.5"
                    ]
                },
                {
                    "name": "priya",
                    "descr": "Endeavour priya partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=priya"
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
                        "env-curl"
                    ]
                },
                {
                    "name": "qcb",
                    "descr": "Endeavour qcb partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=qcb"
                    ],
                    "max_jobs": 1000,
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
                        "env-curl"
                    ]
                },
                {
                    "name": "scec",
                    "descr": "Endeavour scec partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=scec"
                    ],
                    "max_jobs": 5000,
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
                        "env-curl"
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
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-13.3.0-mpich-4.2.2",
            "modules": [
                "gcc/13.3.0",
                "mpich/4.2.2"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
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
                "fio/3.37"
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
        {
            "name": "env-nvhpc-24.5",
            "modules": [
                "nvhpc/24.5"
            ]
        },
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "./logs/reframe-endeavour.log",
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
