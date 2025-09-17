# Endeavour configuration

site_configuration = {
    "general": [
        {
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "logs/endeavour/reports/run-report-$(date --iso-8601=seconds).json"
        }
    ],
    "systems": [
        {
            "name": "endeavour",
            "descr": "Endeavour cluster",
            "stagedir": "logs/endeavour/stage/stage-$(date --iso-8601=seconds)",
            "outputdir": "logs/endeavour/output/output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "endeavour.*"
            ],
            "partitions": [
                {
                    "name": "login",
                    "descr": "Endeavour login nodes",
                    "scheduler": "local",
                    "launcher": "local",
                    "max_jobs": 5,
                    "environs": [
                        "env-none"
                    ]
                },
                {
                    "name": "allnodes",
                    "descr": "Endeavour allnodes partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-9554",
                    "descr": "Endeavour epyc-9554 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-9554"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-9354",
                    "descr": "Endeavour epyc-9354 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-9354"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-9124",
                    "descr": "Endeavour epyc-9124 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-9124"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-7643",
                    "descr": "Endeavour epyc-7643 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-7643"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-7513",
                    "descr": "Endeavour epyc-7513 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-7513"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-7313",
                    "descr": "Endeavour epyc-7313 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-7313"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-7502p",
                    "descr": "Endeavour epyc-7502p nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-7502p"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "epyc-7502",
                    "descr": "Endeavour epyc-7502 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=epyc-7502"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-8358",
                    "descr": "Endeavour xeon-8358 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-8358"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-6348",
                    "descr": "Endeavour xeon-6348 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-6348"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-6338",
                    "descr": "Endeavour xeon-6338 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-6338"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-6226r",
                    "descr": "Endeavour xeon-6226r nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-6226r"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-6148",
                    "descr": "Endeavour xeon-6148 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-6148"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-6130",
                    "descr": "Endeavour xeon-6130 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-6130"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-5118",
                    "descr": "Endeavour xeon-5118 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-5118"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-4116",
                    "descr": "Endeavour xeon-4116 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-4116"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "xeon-2640v4",
                    "descr": "Endeavour xeon-2640v4 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-2640v4"
                    ],
                    "max_jobs": 5000,
                    "environs": [
                        "env-none",
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                }
            ]
        }
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "logs/endeavour/run/reframe.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "logs/endeavour/perf",
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
