# Discovery configuration

site_configuration = {
    "general": [
        {
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "logs/discovery/reports/run-report-$(date --iso-8601=seconds).json"
        }
    ],
    "systems": [
        {
            "name": "discovery",
            "descr": "Discovery cluster",
            "stagedir": "logs/discovery/stage/stage-$(date --iso-8601=seconds)",
            "outputdir": "logs/discovery/output/output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "discovery.*"
            ],
            "partitions": [
                {
                    "name": "login",
                    "descr": "Discovery login nodes",
                    "scheduler": "local",
                    "launcher": "local",
                    "max_jobs": 5,
                    "environs": [
                        "env-none"
                    ]
                },
                {
                    "name": "allnodes",
                    "descr": "Discovery allnodes partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes"
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
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "main",
                    "descr": "Discovery main partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=main"
                    ],
                    "max_jobs": 1000,
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
                        "env-git",
                        "env-fio"
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
                    "max_jobs": 1000,
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
                        "env-git",
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
                    "max_jobs": 1000,
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
                        "env-git",
                        "env-fio"
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
                    "max_jobs": 100,
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
                        "env-git",
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
                        "env-git",
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
                        "env-git",
                        "env-fio"
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
                    "name": "logs/discovery/run/reframe.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "logs/discovery/perf",
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
